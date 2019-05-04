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
            _, boxes, _ = self.env.doAction(agentAction, player.color)
            rewardPoint = 0
            if boxes > 0:
                    player.score += boxes
                    if self.env.isGameOver():
                        rewardPoint = self.env.reward.winReward()
                    else:
                        rewardPoint = self.env.reward.boxReward(boxes)
            else:
                turn = not(turn)
                rewardPoint = 0
            if learn and player.canLearn:
                qClass.updateTable(self.env.prevState,
                                   agentAction,
                                   self.env.currState,
                                   rewardPoint)
    
    def playGameAndLearn(self,qClassInput):
        agent1action = []
        prevState1 = self.env.currState
        agent1action = 0
        totalAgent1Boxes = 0
        agent2action = []
        prevState2 = self.env.currState
        agent2action = 0
        totalAgent2Boxes = 0
        winner = 0 # draw0
        turn = 0
        # agents take turns
        while not self.env.done:
            myTurn = 1
            while myTurn>0 and not self.env.done:
                # agent1 move
#                print("Agent1 move")
                R1 = 0
                # store previous state
                prevState1 = self.env.currState
                # get agent action from policy
                agent1action = self.agent1.getAction(qClassInput,
                                                     self.env.currState,
                                                     self.env.possibleActions())
                # do action and calculate reward
                boxesCompleted1 = self.env.doAction(agent1action)
                R1 = self.reward.reward4box(boxesCompleted1)
                totalAgent1Boxes += boxesCompleted1
                myTurn = boxesCompleted1
                # learn
                qClassInput.updateTable(prevState1,
                          agent1action,
                          self.env.currState,
                          R1)
                turn+=1
            
            # if game finished then exit while loop
            if self.env.done:
                break
            
            myTurn_ = 1
            while myTurn_>0 and not self.env.done:
                # agent2 move
#                print("Agent2 move")
                R2 = 0
                # store previous state
                prevState2 = self.env.currState
                # get agent action from policy
                agent2action = self.agent2.getAction(qClassInput,
                                                     self.env.currState,
                                                     self.env.possibleActions())
                # do action and calculate reward
                boxesCompleted2 = self.env.doAction(agent2action)
                R2 = self.reward.reward4box(boxesCompleted2)
                totalAgent2Boxes += boxesCompleted2
                myTurn_ = boxesCompleted2
                # learn
                qClassInput.updateTable(prevState2,
                                  agent2action,
                                  self.env.currState,
                                  R2)
                turn+=1
            
        # learn from the win
        if totalAgent1Boxes == totalAgent2Boxes:
            winner = 0
        elif totalAgent1Boxes>totalAgent2Boxes:
            winner = 1
        else: # totalAgent1Boxes < totalAgent2Boxes
            winner = 2
        
#        print("boxes:", (totalAgent1Boxes,totalAgent2Boxes))
        
        if winner == 1:
            R1 = self.reward.reward4win()
            # learn
            qClassInput.updateTable(prevState1,
                              agent1action,
                              self.env.currState,
                              R1)
            self.agent1.wins += 1
            print("Winner Agent 1: ", totalAgent1Boxes)
        elif winner == 2:
            qClassInput.updateTable(prevState2,
                          agent2action,
                          self.env.currState,
                          R2)
            self.agent2.wins += 1
            print("Winner Agent 2: ", totalAgent2Boxes)
        else:
            self.agent1.draws += 1
            self.agent2.draws += 1
            print("Draw")
            
        return qClassInput
            