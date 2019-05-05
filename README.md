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
  * 2x2 Play Ground.py - Train and play 2x2 game with Q agent
  * 3x3 Play Ground.py - Train and play 3x3 game with Q agent
  * 2x2FntnPlayGround.py - Train and play 2x2 game with Functional Agent
  * 3x3FntnPlayGround.py - Train and play 3x3 game with Functional Agent
  * agent.py - class for random agent, queue agent and simple agent
  * dotboxenv.py - game environment class
  * gameController.py - game controller that calls the agents and proceeds the game
2. Report - Result Description
3. Results - contains videos of games being played

## Report
[Report.pdf](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Report/Report.pdf)

## Training and Play

### 2x2 board

![2x2 Board](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results/2x2Grid.png)

![2x2 play](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results/2x2Gif.gif)

### Training and Testing Q agent on 2x2 board
1. Open a terminal and goto src folder.
2. Run "2x2 Play Ground.py" file
3. to change number of traing games and number of test games, change the below variables
```
Number_of_Training_Games = 10000
Number_of_Test_Games = 100
```
The results will be printed in the console

### Training and Testing Functional agent on 2x2 board
1. Open a terminal and goto src folder.
2. Run "2x2FntnPlayGround.py" file
3. to change number of traing games and number of test games, change the below variables
```
NoOfEpoh = 10
NoOfSession = 10
Number_of_Test_Games = 100
```
The results will be printed in the console

### 2x2 Game Video

[2x2 Game Video](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results/2x2.avi)

[Additional Videos](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results)

### 3x3 board

![3x3 Board](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results/3x3Grid.png)

![3x3 play](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results/3x3Gif.gif)

### Training and Testing Q agent on 3x3 board
1. Open a terminal and goto src folder.
2. Run "3x3 Play Ground.py" file
3. to change number of traing games and number of test games, change the below variables
```
Number_of_Training_Games = 10000
Number_of_Test_Games = 100
```
The results will be printed in the console

### Training and Testing Functional agent on 2x2 board
1. Open a terminal and goto src folder.
2. Run "3x3FntnPlayGround.py" file
3. to change number of traing games and number of test games, change the below variables
```
NoOfEpoh = 10
NoOfSession = 10
Number_of_Test_Games = 100
```
The results will be printed in the console

### 3x3 Game Video
[3x3 Game Video](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results/3x3.avi)

[Additional Videos](https://github.com/bsaisudh/DotsAndBoxesGame/blob/master/Results)




