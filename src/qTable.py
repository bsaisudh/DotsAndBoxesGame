# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:31:09 2019

@author: balam
"""

import numpy as np
import random
import copy

class qLearn:
    def __init__(self,
                 _allActions,
                 _numActions
                 _learningFactor = 0.1,
                 _discountFactor = 0.3,
                 _epsilon = 0.6):
        self.allActions = _allActions
        self.numAction = _numActions
        self.alpha = _learningFactor
        self.gamma = _discountFactor
        self.epsilon = _epsilon
        self.qTable = dict()
    
    def getDefaultActionWeights():
        return [0]*self.numActions
    
    def updateTable(self,
                    prevState,
                    prevAction,
                    currState,
                    reward):
        prevActionIndex = 
        qPrev = self.qTable[prevState]
        qMax  = np.max(self.qTable[stateIndexCurr,:])
        qNew = qPrev + self.alpha * (reward + self.gamma* qMax - qPrev)
        self.qTable[stateIndexPrev,actionIndexPrev] = qNew
        
    def eGreedyPolicy(self, 
                      currStateIndex,
                      possibleActions):
        pA = copy.deepcopy(possibleActions)
        values = self.qTable[currStateIndex,pA]
        indices = np.where(values == values.max())[0]
        allMaxActions = pA[indices]
        maxAction = random.choice(allMaxActions)
        output = 0
        if random.random() >= self.epsilon or values.shape[0] - indices.shape[0]== 1:
            output = maxAction
        else:
            np.delete(pA,indices)
            output = random.choice(pA)
        return output