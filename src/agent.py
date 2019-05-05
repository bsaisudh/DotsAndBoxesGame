# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:21:14 2019

@author: balam
"""

from qTable import qTable
from dotBoxEnv import dotsBoxesEnv

import random
import numpy as np
from itertools import chain
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier

class agent:
    def __init__(self, _color, _canLearn, _actioDict):
        self.wins = 0
        self.draws = 0
        self.score = 0
        self.totalReward = 0
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
        self.totalReward = 0

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
        

class qFntnAgent(agent):
    def __init__(self,_color, _actioDict, _formatString):
        agent.__init__(self,_color,False, _actioDict)
        self.formatString = _formatString
        
    def init(self, _env:dotsBoxesEnv ):
        self.env = _env
        self.mlpAgent = MLPClassifier(hidden_layer_sizes=(160, 160, 160, 160),
                                     activation='tanh',
                                     warm_start=True, #keep progress between .fit(...) calls
                                     max_iter=1 #make only 1 iteration on each .fit(...)
                                     )
        stateEncoding = [int(x) for x in list(self.formatString.format(self.env.currState))]
        self.mlpAgent.fit([stateEncoding]*self.env.numActions, list(self.env.allActions))
        self.n_actions = self.env.numActions
        self.percentile = 50
        
    def resetSession(self):
        self.states = []
        self.actions = []
        
    def resetBatch(self):
        self.statesBatch = []
        self.actionsBatch = []
        self.rewardBatch = []
        self.log = []
    
    def updateBatch(self):
        self.statesBatch.append(self.states)
        self.actionsBatch.append(self.actions)
        self.rewardBatch.append(self.totalReward)
    
    def selectElites(self):
        rewardThreshold = np.percentile(self.rewardBatch, self.percentile)
        indices = list(np.argwhere(self.rewardBatch > rewardThreshold).flatten())
        self.elite_states  = list(chain(*(np.array(self.statesBatch)[indices]))) # <your code here>
        self.elite_actions = list(chain(*(np.array(self.actionsBatch)[indices])))
        
    def showProgress(self, show):
        mean_reward, threshold = np.mean(self.rewardBatch), np.percentile(self.rewardBatch, self.percentile)
        self.log.append([mean_reward, threshold])
        if show:
            print("mean reward = %.3f, threshold=%.3f"%(mean_reward, threshold))
            reward_range=[-990,+10]
            plt.figure(10,figsize=[8,4])
            plt.subplot(1,2,1)
            plt.plot(list(zip(*self.log))[0], label='Mean rewards')
            plt.plot(list(zip(*self.log))[1], label='Reward thresholds')
            plt.legend()
            plt.grid()
            plt.subplot(1,2,2)
            plt.hist(self.rewardBatch, range=reward_range);
            plt.vlines([np.percentile(self.rewardBatch, self.percentile)], [0], [100], label="percentile", color='red')
#            plt.legend()
            plt.grid()
            plt.show()
    
    
    def getAction(self, 
                  qClass : qTable,
                  currState,
                  possibleActions):
        stateEncoding = list(map(int,list(self.formatString.format(self.env.currState))))
        stateEncoding = np.asanyarray(stateEncoding).reshape(1,-1)
        probs = self.mlpAgent.predict_proba(stateEncoding)[0]
        a = np.random.choice(self.n_actions, 1, p = probs)[0]
        action = 1<<a
        self.states.append(self.env.currState)
        self.actions.append(action)
        return action
    
    