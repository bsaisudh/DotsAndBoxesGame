# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:54:31 2019

@author: balam
"""

from dotBoxEnv import dotsBoxesEnv
from dotBoxEnv import display
from dotBoxEnv import reward
from qTable import qTable
from agent import agent
from agent import qAgent
from agent import randomAgent
from agent import simpleAgent
from gameController import gameController

dbe = dotsBoxesEnv(3)
dp = display(dbe.space, dbe.size, dbe.linePoints, dbe.boxPoints)
qt = qTable(dbe.allActions,dbe.numActions)

agent1 = qAgent([255,0,0], qt.actionDict) #blue
agent2 = qAgent([0,255,0], qt.actionDict) #green
agent1.islearning = True
agent2.islearning = True
dbe.disp.updateDisplay = False
game = gameController(dbe, agent1, agent2)
for gameNo in range(10000):
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
for gameNo in range(100):
    game.reset()
    game.play(qt, False)
    game.distributeTropy()
print("*********","a1:", agent1.wins, " a2:", agent2.wins, " draw:" , agent1.draws)

dp.show()
dp.releaseVideo()
dp.waitAndDestroy()

