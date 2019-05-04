# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:31:09 2019

@author: balam
"""

import numpy as np
import random
import copy

class qTable:
    def __init__(self,
                 _allActions,
                 _numActions,
                 _learningFactor = 0.7,
                 _discountFactor = 0.6,
                 _epsilon = 0.6):
        
        self.numActions = _numActions
        self.alpha = _learningFactor
        self.gamma = _discountFactor
        self.epsilon = _epsilon
        self.defaultActWt = self.getDefaultActionWeights()
        self.getActionDict(_allActions)
        self.qTable = dict()
        
    def getActionDict(self, allActions):
        self.actionDict = dict()
        for ndx,action in enumerate(allActions):
            self.actionDict[action] = ndx

    def getDefaultActionWeights(self):
        return tuple([0]*self.numActions)
    
    def updateTable(self,
                    prevState,
                    prevAction,
                    currState,
                    reward):
        #use defaut if not found
        qPrevAll = list(self.qTable.setdefault(prevState, self.defaultActWt))
        prevActNdx = self.actionDict[prevAction]
        qPrev = qPrevAll[prevActNdx]
        qPrevMax  = max(self.qTable.setdefault(currState, self.defaultActWt))
        qNew = qPrev + self.alpha * (reward + self.gamma* qPrevMax - qPrev)
        qPrevAll[prevActNdx] = qNew
        self.qTable[prevState] = tuple(qPrevAll)
        
    def eGreedyPolicy(self, 
                      currState,
                      possibleActions):
        qVals = self.qTable.setdefault(currState, self.defaultActWt)
        posQvals = [qVals[self.actionDict[act]] for act in possibleActions]
        maxNdx = posQvals.index(max(posQvals))
        maxAct = possibleActions[maxNdx]
        finalAct = 0
        if random.random() >= self.epsilon:
            finalAct = maxAct
        else:
            finalAct = possibleActions.pop(maxNdx)
            if len(possibleActions) == 1 :
                finalAct = possibleActions[-1]
            elif len(possibleActions) > 1:
                finalAct = possibleActions[random.randint(0,len(possibleActions)-1)]
                
        return finalAct