# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:54:31 2019

@author: balam
"""

Number_of_Training_Games = 10000
Number_of_Test_Games = 100


from dotBoxEnv import dotsBoxesEnv
from dotBoxEnv import display
from dotBoxEnv import reward
from qTable import qTable
from agent import agent
from agent import qAgent
from agent import randomAgent
from agent import simpleAgent
from gameController import gameController
from matplotlib import pyplot as plt

dbe = dotsBoxesEnv(3)
qt = qTable(dbe.allActions,dbe.numActions)

agent1 = qAgent([255,0,0], qt.actionDict) #blue
agent2 = qAgent([0,255,0], qt.actionDict) #green
agent1.islearning = True
agent2.islearning = True
dbe.disp.updateDisplay = False
game = gameController(dbe, agent1, agent2)
for gameNo in range(Number_of_Training_Games):
    game.reset()
    game.play(qt, True)
    game.distributeTropy()
#    print("a1: ",agent1.score," a2: ", agent2.score, " draw: ", agent1.draws)
#    dbe.disp.waitForUser()
    if gameNo%100 == 0:
        print("iterations:" , gameNo ,"a1:", agent1.wins, " a2:", agent2.wins, " draw:" , agent1.draws)
    
print("a1:", agent1.wins, " a2:", agent2.wins, " draw:" , agent1.draws)

agent1 = randomAgent([255,0,0], qt.actionDict) #blue
agent2 = qAgent([0,255,0], qt.actionDict) #green
agent1.islearning = False
agent2.islearning = False
dbe.disp.updateDisplay = True
game = gameController(dbe, agent1, agent2)
scoreQ = []
scoreR = []
for gameNo in range(Number_of_Test_Games):
    game.reset()
    game.play(qt, False)
    game.distributeTropy()
    scoreQ.append(agent2.score)
    scoreR.append(agent1.score)
print("********************")
print("a1:", agent1.wins, " a2:", agent2.wins, " draw:" , agent1.draws)
print("a1 Mean Score : ", sum(scoreR)/len(scoreR),
      " a2 Mean Score : ", sum(scoreQ)/len(scoreQ))
plt.plot(scoreQ,"r")
plt.plot(scoreR,"b")
plt.show()

dbe.disp.releaseVideo()

