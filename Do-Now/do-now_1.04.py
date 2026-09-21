#Do Now 1.04
#String Concatenation and Formatting

#Why is concatenation so time consuming?
#You probably noticed that concatenating a string with variables and other strings is...a hassle
#It shouldn't take so long to complete the process of concatenating, but we have to account for all this syntax in a sentence!
#Something we can do to help this process is to learn some formatting tips!
#Formatting can help us get the job done will also being explicit with our computers to do the thing we want done

#Instructions shouldn't be so complicated and time consuming however!
#Perhaps there is a faster way to do all this string concatenating
#We are going to check out a few different ways to make our job easier

#F-string formatting
#f-string formatting is a nice, compact way to concatenate a bunch of variables
#into a larger string
#Special sytax needed: {} and the letter f
#Let's check it out!
name = input('What is your name? ')
score = str(8)
print(f'The total score for {name} is {score}.')
#Notice that the braces contain the variable names that are replaced in the larger string with their string value
#Pros: compact and pretty straightforward!
#Cons: we still need to insert spaces into the larger string

#Parameters
#Parameters are a way of using arguments in a function for execution
#You are used to parameters in the print() function: it is typically a big ol' string
#Think about this example:
#print('The ' + speed + ' brown fox jumped over the lazy dog.')
#Pretty easy way to think of the parameter: it is what we put in the parentheses of our function
#most functions can take multiple parameters though! And we can have the print function take
#in multiple parameters and do the work for us.
#Special syntax needed: commas!
#Let's check it out!
#person = input('What is your name? ')
#total = str(12)
#print('The total score for', person, 'is', total)
#Notice: we do comma separation between our various arguments
#Pros: compact; spaces are already accounted for
#Cons: still need to explicitly state any punctuation in the function

#Try it out!
#Write two different input functions that take in strings
#Choose a formatting option above that interests you
#Try formatting in a print function to simplify the task of concatenation
