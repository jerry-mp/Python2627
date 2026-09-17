#Do Now 1.03 
#Inputs

#Overview
#In this Do Now, we will cover a new function, input()

#The input function
#The input function allows users to provide information in the console that can be used within the program
#NOTE: the default data type that input takes in is a string! So, this will require us to focus on casting, if need be

#Example 1
#Uncomment the following 2 lines of code
#a = input('What is your name? ')
#print('Hello there, ' + a)
#Input allows us to send data/information to our Python program to do something with it!

#Example 2
#Uncomment the following 5 lines of code
# print('Welcome to the Basic Calculator! I can add numbers!')
# number1 = int(input('Enter a value: '))
# number2 = int(input('Enter a second value: '))
# value = number1 + number2
# print('Your sum is ' + str(value))

#Example 3 - You Do It!
#Try writing a variable that is assigned an input that takes in a number from the user
#Use that number to do some basic math
#print back the answer using casting
#Check out Example 2 if you need some direction!

#Casting
#In this activity, we've seen a few types of casting
#String-to-integer casting, using int()
#Integer-to-string casting, using str()
#Python likes data types working with its own kin - we typically can't mix them up!
#Since input() defaults to string inputs, we sometimes have to cast any information
#that is going to be used for computations, etc.
#Casting always wraps the specific data type that it needs to convert
#This is why we see int(input()) often -- we are usually changing user inputs into integers
#Over time, we will learn other types of casting for different scenarios.