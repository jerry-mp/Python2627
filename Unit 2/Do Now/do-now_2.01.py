#Do Now 2.01
#Casting

#Overview
#In this lesson, we will cover the idea of casting a bit more deeply.
#As you remember, casting is the process of converting one data type to another for the purpose of doing something with that data in our program

#Type and Types of Casting
#Python has a nice built in function, type(), that we can use to test the type of specific data. Try commenting out the next line and running the program
# print(type('The quick brown fox jumped over the lazy dog'))
#Output (what came out in the console?): 

#The type() function can be quite useful for checking a data type that might be giving you some troulbe in your program! How about we check out how this works in the next three lines
# age = 12
# user_age = print('your age is' + age)
# print(type(age))
#This might be a pretty 'simple' one to check out, but it might be a more complicated issue in the future

#Casting Basics
#When casting, we want to ultimately ask ourselves: what do I need to cast this data for?
#In some settings, casting is completely arbitrary or evening pointless!
#We wouldn't want to cast a string to an integer to concatenate into a larger string because concatenation is only done with strings
#Similiarly, we can't cast a string into a numeric value:
#print(int('hello'))
#Code above only works if hello was in decimal/base-10 numbers, which it is not!

#What Data Types can I cast to?
# There are four basic castings to note at this point:
# 1. string: uses str() to convert data to strings
# 2. integer: uses int() to convert inputs/and other numeric data into integers
# 3. float: uses float() to convert inputs/and other numeric data into floats (decimals)
# 4. boolean: uses bool() to convert data into True/False outcomes

#Try it out
#Uncomment the following lines of code to test their outputs. Record the outputs
# 1.
#value = int('73')
#print(value)
#print(type(value))
# Output:
# 2. 
#number = str(73)
#print(number)
#print(type(number))
# Output:
# 3.
#remainder = float(55)
#print(remainder)
#print(type(remainder))
# Output:
# 4.
#answer = bool(92)
#print(answer)
#print(type(answer))
# Output