#Do Now 2.06: While Loops
import math
#Overview: In this do now, we will be introduced to the concept of a while loop. A while loop allows a program to run and execute a process for a determined amount of time based on conditions for its execution

#Objectives
#1. Learn the basic syntax of a while loop
#2. Cover strategies for a while loop's implementation in a program

#Example 1: Read the code below, then uncomment. What does this code block feature? What does it do?
# print_loop = True
# while print_loop:
	# print('a')
	
# Example 2: You may have noticed that the last loop can get a little out of hand if you are not careful. Read the code below, then uncomment. What does this code block feature? What does it do?
# counter = 0
# while counter < 10:
	# print('Hello!')
	
# Example 3: You may have noticed that not much changed from Example 1 to Example 2. Read the code below, then uncomment. What does this code block feature? What does it do?
# counter = 0
# while counter < 10:
    # print('Hello!')
    # counter += 1
    
#Example 4: Now, we should begin to learn how to use loops in a way that is useful for settings in which we want the loop to end based on specific criteria, or conditions, that are met. Read the code below, then uncomment. What does this code block feature? What does it do?
# quitgame = 'n'
# while quitgame != 'y':
    # print("Hello!")
    # quitgame = input("Would you like to quit the game (y or n)? ").lower()
    
#Task 1: Create a basic while loop that: 1) asks the user for a number that will be multiplied by 2; 2) after each input question, the program prints out the product of their number and 2; 3) the program runs until the user inputs 'stop'
# math_loop = True
# while math_loop:
    # user_input = input('Enter a number to multiply by 2 (stop to cancel): ')
    # if user_input == 'stop':
        # math_loop = False
    # else:
        # print(int(user_input)*2)

#Task 2: Create a basic while loop that: 1) has 9 total turns; 2) asks two different users for a number between 1 and 10; 3) compares the two numbers and declares a winner each turn; 4) updates the turn number after each turn; 5) the loop stops after the turns are over
n = math.sqrt(2)
round_n = round(n,25)
print(round_n)
game_counter = 0
print('Both players will pick a number between 1 and 10. The player with the highest number wins that round.')
while game_counter < 9:
    player1 = int(input('Pick a number between 1 and 10: '))
    player2 = int(input('Pick a number between 1 and 10: '))
    if player1>player2:
        print('Player1 WINS')
    elif player1<player2:
        print('Player2 WINS')
    else:
        print('TIE')