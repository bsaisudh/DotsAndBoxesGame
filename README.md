# DotsAndBoxesGame

Dots and boxes game for 2x2 and 3x3 configuration are played using Q Learning.

### Prerequisites

The code is implemented in Python and has the following Dependency :
1. Python 3
2. Scikit library for python

### Cloning the repositort form git

Execute the following command:
```
git clone https://github.com/bsaisudh/DotsAndBoxesGame.git
```

### File Structure

The project directory structure is as follows:
1. src - Contains the source code Files
  * 2x2 Play Ground.py - Train and play 2x2 game
  * 3x3 Play Ground.py - Train and play 3x3 game
  * agent.py - class for random agent, queue agent and simple agent
  * dotboxenv.py - game environment class
  * gameController.py - game controller that calls the agents and proceeds the game
2. Report - Result Description
3. Results - contains videos of games being played

## Report
 [Report.pdf](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Report/Report.pdf)

## Training and Play

### 2x2 board
1. Open a terminal and goto src folder.
2. Run "3x3 Play Ground.py" file
3. to change number of traing games and number of test games, change the below variables
```
Number_of_Training_Games = 10000
Number_of_Test_Games = 100
```
The results will be rinted in the console

[3x3 Game Video](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results/3x3.avi)


### 2x2 board
1. Open a terminal and goto src folder.
2. Run "2x2 Play Ground.py" file
3. to change number of traing games and number of test games, change the below variables
```
Number_of_Training_Games = 10000
Number_of_Test_Games = 100
```
The results will be rinted in the console




