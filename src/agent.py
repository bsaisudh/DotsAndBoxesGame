# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:21:14 2019

@author: balam
"""

from qTable import qTable
import random

class agent:
    def __init__(self, _color, _canLearn, _actioDict):
        self.wins = 0
        self.draws = 0
        self.score = 0
        self.color = _color
        self.canLearn = _canLearn
        self.actionDict = _actioDict
        self.islearning = True
    
    def getAction(self, 
                  qClass : qTable,
                  currState,
                  possibleActions):
        pass
    def reset(self):
        self.score = 0

class qAgent(agent):
    def __init__(self,_color, _actioDict):
        agent.__init__(self,_color,True, _actioDict)
    
    def getAction(self, 
                  qClass : qTable,
                  currState,
                  possibleActions):
        if self.islearning:
            return qClass.eGreedyPolicy(currState,possibleActions)
        else:
            qVals = qClass.qTable.setdefault(currState)
            posQvals = [qVals[self.actionDict[act]] for act in possibleActions]
            maxNdx = posQvals.index(max(posQvals))
            maxAct = possibleActions[maxNdx]
            return maxAct
    
    
class randomAgent(agent):
    def __init__(self,_color, _actioDict):
        agent.__init__(self,_color,False, _actioDict)
    
    def getAction(self, 
                  qClass : qTable,
                  currState,
                  possibleActions):
        actionIndex = random.randint(0,len(possibleActions)-1)
        return possibleActions[actionIndex]

class simpleAgent(agent):
    def __init__(self,_color, _actioDict):
        agent.__init__(self,_color,False, _actioDict)
    
    def getAction(self, 
                  qClass : qTable,
                  currState,
                  possibleActions):
        return possibleActions[0]
        
        
        