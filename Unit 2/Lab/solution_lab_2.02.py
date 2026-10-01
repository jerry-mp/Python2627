#Lab 2.02 - Booleans
#Name:

#Overview
#This lab will focus on the basics of booleans, which you have started to learn this week!
#Complete each part as completely as possible!

#Part 1: Predict
#Instructions: Read each example below. Make a prediction: what will the output in the console be? After running the example, record the actual output

#Example 1
#a = 100
#b = 'science'
#print(a > 75 and b == 'science')
#prediction:
#Output:

#Example 2
#a = 100
#b = 'science'
#print(a > 75 and b != 'science')
#prediction:
#Output:

#Example 3
#a = 100
#b = 'science'
#print(a > 75 or b != 'science')
#prediction:
#Output:

#Example 4
#a = 100
#b = 'science'
#c = True
#print(not c and a > 75 and b == 'science')
#prediction:
#Output

#Part 2: Create
#In the space below, write a short 'Can I be President?' program. The program will check to see if the user meets the minimum requirements for becoming President of the United States. Have the user input the information needed.
#HINT: Refer to do-now_2.02.py for any tips on how to set this up!

#Requirements to be president:
#Older than 35
#Resident of US for 14 years
#Natural born citizen
#Print True if the user can be President, and False if not
# age = 35
# years_a_resident = 14
# citizen = 'yes' #without using if/else yet

# user_age = int(input('How old are you? '))
# user_resident = int(input('How many years have you resided in the country? '))
# user_citizen = input('Are you a natural born citizen of the USA? ')
# print(user_age >= age and user_resident >= years_a_resident and user_citizen == citizen)

#Bonus: Create
#Create a 'Can I ride the roller coaster?' program. It will check to see if the user meets the minimum requirements to ride the roller coaster. have the user input the information needed.

#Requirements to ride the roller coaster:
#Height over 50 inches - loophole allows any height if older than 18
#Each ride costs 4 quarters
#There is a frequent rider pass, which makes the ride only cost 2 quarters
#Print True if the user can ride the roller coaster, and False if not.
# height = 50
# cost = 4
# loophole = 18
# rider_pass = 'yes'

# user_height = int(input('How tall are you, in inches? '))
# user_money = int(input('How many quarters do you have? '))
# user_age = int(input('How old are you? '))
# user_pass = input('Do you have a frequent rider pass? ')
# print((user_height >= height and user_money >= cost) or (user_height != height and user_age >= loophole and user_money  >= cost) or (user_height >= height and user_money >= 2 and user_pass == rider_pass) or (user_height != height and user_money >= 2 and user_pass == rider_pass and user_age >= loophole))
#booleans suck without conditionals!!!