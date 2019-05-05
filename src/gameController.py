# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:55:31 2019

@author: balam
"""

from dotBoxEnv import dotsBoxesEnv
from dotBoxEnv import reward
from qTable import qTable
from agent import agent
from agent import qAgent
from agent import randomAgent
from agent import simpleAgent


class gameController:
    def __init__(self, 
                 _env: dotsBoxesEnv, 
                 _agent1:agent, 
                 _agent2:agent):
        self.env = _env
        self.agent1 = _agent1
        self.agent2 = _agent2
    
    def reset(self):
        self.env.reset()
        self.agent1.reset()
        self.agent2.reset()
    
    def distributeTropy(self):
        if self.agent1.score == self.agent2.score:
            self.agent1.draws += 1
            self.agent2.draws += 1
        elif self.agent1.score > self.agent2.score:
            self.agent1.wins += 1
        else:
            self.agent2.wins += 1
        
    def play(self, qClass:qTable, learn):
        players = [self.agent1, self.agent2]
        turn = True # True = P1 ; False = P2
        while not(self.env.isGameOver()):
            player = players[int(turn)]
            agentAction = player.getAction(qClass,
                                      self.env.getCurrentState,
                                      self.env.getPossibleActions())
            _, boxes, error = self.env.doAction(agentAction, player.color)
            rewardPoint = 0
            if error:
                rewardPoint = self.env.reward.invalidMoveReward()
                player.totalReward +=rewardPoint
            else:
                if boxes > 0:
                        player.score += boxes
                        if self.env.isGameOver():
                            rewardPoint = self.env.reward.winReward()
                            player.totalReward +=rewardPoint
                        else:
                            rewardPoint = self.env.reward.boxReward(boxes)
                            player.totalReward +=rewardPoint
                else:
                    turn = not(turn)
                    rewardPoint = 0
            if learn and player.canLearn:
                qClass.updateTable(self.env.prevState,
                                   agentAction,
                                   self.env.currState,
                                   rewardPoint)
            