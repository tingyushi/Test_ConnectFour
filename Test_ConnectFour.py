'''
How to use the testing file
1. install pynput library first (this is a python library, you can use pip or pip3 to install)
    This is a library to simulate user keyboard inputs

2. put the following files in the same folder
   ConnectFour.java
   Player.java
   Board.java
   AIPlayer.java
   HumanPlayer.java
   Runner_Human.java
   Runner_AI.java
   Test_ConnectFour.py

3. Open your terminal and change the directory to the folder you created in step2 (use cd commad)

4. type "python3 A1_Test.py 1" to compile all your .java files, then you will see .class files in the folder

5. type "python3 A1_Test.py 4" to test horizontal win condition

6. type "python3 A1_Test.py 5" to test vertical win condition

7. type "python3 A1_Test.py 6" to test diagonal(up right) win condition

8. type "python3 A1_Test.py 7" to test diagonal(up left) win condition

9. type "python3 A1_Test.py 8" to test tie condition

10. type "python3 A1_Test.py 9" to start AI test (you have to test AIPlayer manually)
'''

from subprocess import run
from pynput.keyboard import Key, Controller
from threading import Thread
import time
import sys

class Runner_Human(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        command = ["java", "Runner_Human"]
        run(command)


# simulate user inputs so that one player can win verically
class Runner_Human_Input_Vertical(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        time.sleep(0.5)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
        time.sleep(0.5)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
        time.sleep(0.5)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

# simulate user inputs so that one player can win horizontally
class Runner_Human_Input_Horizontal(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        time.sleep(0.5)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('4')
        keyboard.release('4')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


# simulate user inputs so that one player can win diagonally (up-right)
class Runner_Human_Input_Diagonal_up_right(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        time.sleep(0.5)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('4')
        keyboard.release('4')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('4')
        keyboard.release('4')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('5')
        keyboard.release('5')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('4')
        keyboard.release('4')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('5')
        keyboard.release('5')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('5')
        keyboard.release('5')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('7')
        keyboard.release('7')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('5')
        keyboard.release('5')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    

class Runner_Human_Input_Diagonal_up_left(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        time.sleep(0.5)
        keyboard.press('6')
        keyboard.release('6')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('5')
        keyboard.release('5')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('5')
        keyboard.release('5')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('4')
        keyboard.release('4')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('4')
        keyboard.release('4')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('4')
        keyboard.release('4')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(0.5)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


#simulate inputs to make a tie
class Tie_Inputs(Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        time.sleep(0.5); keyboard.press('2'); keyboard.release('2')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('1'); keyboard.release('1')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('7'); keyboard.release('7')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('7'); keyboard.release('7')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('7'); keyboard.release('7')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('1'); keyboard.release('1')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('2'); keyboard.release('2')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('4'); keyboard.release('4')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('4'); keyboard.release('4')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('1'); keyboard.release('1')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('1'); keyboard.release('1')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('4'); keyboard.release('4')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('2'); keyboard.release('2')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('2'); keyboard.release('2')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('2'); keyboard.release('2')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('5'); keyboard.release('5')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('7'); keyboard.release('7')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('4'); keyboard.release('4')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('3'); keyboard.release('3')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('1'); keyboard.release('1')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('7'); keyboard.release('7')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('7'); keyboard.release('7')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('3'); keyboard.release('3')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('5'); keyboard.release('5')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('1'); keyboard.release('1')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('4'); keyboard.release('4')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('4'); keyboard.release('4')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('3'); keyboard.release('3')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('6'); keyboard.release('6')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('2'); keyboard.release('2')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('3'); keyboard.release('3')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('3'); keyboard.release('3')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('5'); keyboard.release('5')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('3'); keyboard.release('3')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('6'); keyboard.release('6')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('5'); keyboard.release('5')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('6'); keyboard.release('6')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('6'); keyboard.release('6')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('6'); keyboard.release('6')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('5'); keyboard.release('5')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('6'); keyboard.release('6')
        keyboard.press(Key.enter); keyboard.release(Key.enter)

        time.sleep(0.5); keyboard.press('5'); keyboard.release('5')
        keyboard.press(Key.enter); keyboard.release(Key.enter)


keyboard = Controller()

'''
1 --> compile all the files
2 --> remove all class files
3 --> remove submissions
4 --> test horizontal win condition
5 --> test vertical win condition
6 --> test diagonal win condition (up right)
7 --> test diagonal win condition (up left)
8 --> test tie 
9 --> test AI Player
'''

indicator = eval(sys.argv[1])

if indicator == 1:
    command1 = ["javac", "Runner_AI.java"]
    command2 = ["javac", "Runner_Human.java"]
    run(command1)
    run(command2)

if indicator == 2:
    command = ["rm", "AIPlayer.class", "HumanPlayer.class", "Board.class", 
               "ConnectFour.class", "Player.class", "Runner_AI.class", "Runner_Human.class"]
    run(command)

if indicator == 3:
    command = ["rm", "AIPlayer.java", "HumanPlayer.java", "Board.java"]
    run(command)

if indicator == 4:
    game = Runner_Human()
    user_inputs = Runner_Human_Input_Horizontal()
    game.start()
    user_inputs.start()
    game.join()
    user_inputs.join()

if indicator == 5:
    game = Runner_Human()
    user_inputs = Runner_Human_Input_Vertical()
    game.start()
    user_inputs.start()
    game.join()
    user_inputs.join()

if indicator == 6:
    game = Runner_Human()
    user_inputs = Runner_Human_Input_Diagonal_up_right()
    game.start()
    user_inputs.start()
    game.join()
    user_inputs.join()

if indicator == 7:
    game = Runner_Human()
    user_inputs = Runner_Human_Input_Diagonal_up_left()
    game.start()
    user_inputs.start()
    game.join()
    user_inputs.join()

if indicator == 8:
    game = Runner_Human()
    user_inputs = Tie_Inputs()
    game.start()
    user_inputs.start()
    game.join()
    user_inputs.join()

if indicator == 9:
    command = ["java", "Runner_AI"]
    run(command)