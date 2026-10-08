#Do Now 2.03 - Conditionals

#Overview
#In this lesson, we will be introduced to conditionals in Python!

#Think about the following program scenario:
#Write a program that keeps a schedule
#This program asks the user for what hour of the day it is
#The program uses this input to tell the user where they should be at this time
#Example:
#What hour is it? 12pm
#You should be at lunch!

#Given what you know so far, how hard would it be to write this program? What else would be helpful to accomplish this?

#Conditionals
#Conditionals are a way to control the flow of a program through ensuring specific criteria are meet in order to trigger a part of our code
#The basic idea around a conditional is to check whether or not something is true/false; using the idea of a boolean, this allows the program to continue/execute parts of our code that wouldn't be executed without the conditions being met
#Here are the basic conditionals in Python:
#if - this is the first condition we will use; it checks for a specific criteria
#elif - this is a secondary condition that is checked if the first condition is not met, and so on and so forth
#else - this is a sort of catch all; if no previous conditions are met, then the else is triggered
#All conditionals use a new piece of syntax, the colon (:), and this, as we will see, neccessitates the use of indentation (the result of the condition)

#Example 1
#Let's check out a basic use of conditions using if
# x = int(input('Enter a number: '))
# if x > 0:
	# print('Your number is positive.')
# else:
	# print('Your number is negative.')
    
#Example 2
#Read the code below. What do we expect the output of the code to be?
# animal = input('What is your favorite animal? ')
# if animal == 'cat' or animal == 'dog':
    # print('A great pet!')
# else:
    # print('Good choice')

#Example 3
#Let's change the code from example 2 just a little bit and see what happens now
# animal = input('What is your favorite animal? ')
# if animal == 'cat' or animal == 'dog':
    # print('A great pet!')
# elif animal == 'hamster':
    # print('Cute!')
# else:
    # print('Good choice')
    
#Create!
#It is time to try your hand at a conditional now!
#Write a brief program that:
# 1) asks the user how old they are; 
#2) if the user is older than 18, tell them they can buy the movie ticket; 
#3) if the user is younger than 18, tell them they need a parent to buy the ticket
