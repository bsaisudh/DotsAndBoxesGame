# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:54:31 2019

@author: balam
"""

Number_of_Training_Games = 100
Number_of_Test_Games = 100


from dotBoxEnv import dotsBoxesEnv
from dotBoxEnv import display
from dotBoxEnv import reward
from qTable import qTable
from agent import agent
from agent import qAgent
from agent import randomAgent
from agent import simpleAgent
from agent import qFntnAgent
from gameController import gameController

dbe = dotsBoxesEnv(3)
qt = qTable(dbe.allActions,dbe.numActions)

agent1 = randomAgent([255,0,0], qt.actionDict) #blue
agent1.islearning = True

formatString = "{0:0>24b}"
agent2 = qFntnAgent([0,255,0], qt.actionDict, formatString) #green
agent2.init(dbe)
agent2.resetBatch()
agent2.resetSession()
agent2.islearning = True

dbe.disp.updateDisplay = True

game = gameController(dbe, agent1, agent2)

for session in range(500):
    for gameNo in range(Number_of_Training_Games):
        agent2.resetSession()
        game.reset()    
        game.play(qt, True)
        game.distributeTropy()
        agent2.updateBatch()
    #    print("a1: ",agent1.score," a2: ", agent2.score, " draw: ", agent1.draws)
    #    dbe.disp.waitForUser()
        if gameNo%100 == 0:
            dbe.disp.updateDisplay = True
            agent2.showProgress(False)
            print("iterations:" , gameNo ,"a1:", agent1.wins, " a2:", agent2.wins, " draw:" , agent1.draws)
        else:
            agent2.showProgress(False)
            dbe.disp.updateDisplay = False
    agent2.selectElites()
    eliteStates = [list(map(int,list(agent2.formatString.format(state)))) for state in agent2.elite_states]
    agent2.mlpAgent.fit(eliteStates, agent2.elite_actions)

    agent2.showProgress(True)

    

print("a1:", agent1.wins, " a2:", agent2.wins, " draw:" , agent1.draws)

#agent1 = randomAgent([255,0,0], qt.actionDict) #blue
#agent2 = qAgent([0,255,0], qt.actionDict) #green
agent1.wins = 0
agent2.wins = 0
agent1.draws = 0
agent2.draws = 0
game.reset()
agent1.islearning = False
agent2.islearning = False
dbe.disp.updateDisplay = True
game = gameController(dbe, agent1, agent2)
for gameNo in range(Number_of_Test_Games):
    game.reset()
    game.play(qt, False)
    game.distributeTropy()
print("*********","a1:", agent1.wins, " a2:", agent2.wins, " draw:" , agent1.draws)

dbe.disp.releaseVideo()
