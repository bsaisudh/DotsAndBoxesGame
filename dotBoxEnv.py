# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 01:37:59 2019

@author: balam
"""

import numpy as np
import itertools
import cv2

class dotsBoxesEnv:
    def __init__(self,
                  _size = 2):
        self.boxPoints = dict()
        self.linePoints = dict()
        self.size = _size
        self.numActions = (self.size+1) * self.size * 2
        self.numStates = 2 ** (self.numActions)
        self.allStates = list(range(self.numStates))        
        self.allActions = []
        self.getSpace()
        self.getLinePoints()
        self.currState = self.allStates[0]
        self.prevState = None
        self.allBoxes = self.getallBoxes()
        
    def getLinePoints(self):
        for item in range(self.numActions):
            action = 1 << item
            self.allActions.append(action)
            pos = np.where(self.space == item+1)
            pos = (pos[0][0],pos[1][0])
            columnsInRow = [self.size , self.size+1]*self.size
            columnsInRow.append(self.size)
            temp = item
            for ndx,val in enumerate(columnsInRow):
                temp = temp - val
                if temp < 0:
                    if ndx%2 == 0:
                        self.linePoints[action] = [[pos[1]-1, ndx], [pos[1]+1,ndx]]
                    else:
                        print(ndx)
                        print(pos)
                        self.linePoints[action] = [[pos[1], ndx-1], [pos[1],ndx+1]]
                    break
        
    def getSpace(self):
        a = [x for x in range(1,self.numActions+1)]
        b = [0] * self.numActions
        self.space = list(itertools.chain(*zip(b,a)))
        self.space.append(0)
        self.spaceSize = ((self.size*2)+1 , (self.size*2)+1)
        self.space = np.asarray(self.space).reshape(self.spaceSize)
        
    def possibleActions(self):
        possActions = [action for action in self.allActions if (self.currState | action) == 0]
        return possActions

    def doAction(self, action):
        currState = self.currState | action
        error = (currState | action) == currState
        if not error:
            self.prevState = self.currState
            self.currState = currState
        numFilledBoxes = self.getNumFilledBoxes(action)
        return self.currState, numFilledBoxes, error
    
    def getallBoxes(self):
        zero = np.where(self.space == 0)
        boxPos = [[x,y] for x,y in zip(zero[0],zero[1])]
        boxes = []
        boxAction = [[-1,0],[1,0],[0,-1],[0,1]]
        for box in boxPos:
            boxBin = 0
            for act in boxAction:
                x , y = box[0]+act[0] , box[1]+act[1]
                if x >= 0 and y >= 0 and x < self.spaceSize[0] and y < self.spaceSize[1] and box[0]%2!=0 and box[1]%2!=0:
                    boxBin = boxBin | (1 << self.space[x,y])
                else:
                    boxBin = 0
                    break
            if boxBin:
                boxes.append(boxBin)
                self.boxPoints[boxBin] = box
        return boxes
        
    def gameOver(self):
        return self.currState == self.allStates[-1]
    
    def getNumFilledBoxes(self,action):
        count = 0
        for box in self.allBoxes:
            if box & action:
                count+=1
        return count
    
    def reset(self):
        self.currState = self.allStates[0]
    
class display:
    def __init__(self,_space,_size, _actLines, _boxes):
        self.space = _space
        self.size = _size
        self.boxes = _boxes
        self.actLines = _actLines
        self.gridSize = 0.005
        self.imgSize = (int(self.size/self.gridSize), int(self.size/self.gridSize))
        self.xOffset = int(self.imgSize[0]*0.2)
        self.yOffset = int(self.imgSize[1]*0.2)
        self.boxSize = (self.toImgCoord(0,0)[0] - self.toImgCoord(2,2)[0])*0.8
        self.gameBoard = np.multiply(np.ones((self.imgSize[0], 
                                              self.imgSize[1],
                                              3)),255).astype('uint8')
#        self.video = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*"XVID"), 50,self.imgSize)
        self.video = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, self.imgSize)
        self.initGameBoard()
        
    
    def toImgCoord(self, x,y):
        return (int((x/self.gridSize)*0.2) + self.xOffset ,
                int((y/self.gridSize)*0.2) + self.yOffset)

    def initGameBoard(self):
        zero = np.where(self.space == 0)
        for x,y in zip(zero[0],zero[1]):
            if x%2==0 and y%2==0:
                self.gameBoard = cv2.circle(self.gameBoard,
                                            self.toImgCoord(x,y),
                                            int(0.03/self.gridSize),
                                            [0,0,255],
                                            thickness=-1)
    
    def addAction(self, action):
        pts = self.actLines[action]
        pt1 = pts[0]
        pt2 = pts[1]
        self.gameBoard = cv2.line(self.gameBoard,
                                 self.toImgCoord(pt1[0],pt1[1]),
                                 self.toImgCoord(pt2[0],pt2[1]),
                                 [255, 0, 0],
                                 thickness = int(0.01/self.gridSize))
    
    def addBox(self, boxBin, color):
        boxCenter = self.boxes[boxBin]
        pt = self.toImgCoord(boxCenter[0],boxCenter[1])
        pt1 = (int(pt[0]-self.boxSize/2), int(pt[0]-self.boxSize/2))
        pt2 = (int(pt[0]+self.boxSize/2), int(pt[1]+self.boxSize/2))
        self.gameBoard = cv2.rectangle(self.gameBoard, pt1, pt2, color, thickness=-1)
    
    def show(self):
        cv2.imshow("DotAndBox", self.gameBoard)
        self.video.write(self.gameBoard)
        cv2.waitKey(1)

    def waitForUser(self):
        while(0):
            pressed = cv2.waitKey(10)
            if  pressed == ord('n'):
                return False
            elif pressed == ord('q'):
                return True
            else:
                continue

    def releaseVideo(self):
        self.video.release()
    
    def waitAndDestroy(self):
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        