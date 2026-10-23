#Do Now 2.04 - Lists

#Objective
#In this do now, you will be introduced to a new data type in Python: lists!
#You will also learn:
#1. Key parts of lists: item, index, and integer
#2. Access items from a list using an index
#3. Use a list to store other data types
#4. Use the function len() to determine the size of a list (how many items in the list)

#Example 1: Uncomment the next two lines of code; what does the len() function do?
# a_list = ['a', 'b', 'c', 'd', 'e']
# print(len(a_list))
# print(a_list[0])
# print(a_list)
# print(a_list[3])
# print(a_list[-1000])
#What is unique about the data stored in a_list?

#What is a List?
#A list is a data type that stores a sequence of values
#The values in a list are called 'elements' or 'items'
#A list has a sequence order that is related to what position a given item holds in the list. This placement is called the item's index
#All lists in Python are 0-indexed, meaning they count their items starting at zero
#The range of the index of a list starts at 0 and counts until we have no more items to count

#Consider the following list
#animals = ['cat', 'dog', 'elephant', 'tiger', 'walrus', 'orangutan', 'eagle']
#How many items are in this list?
#What would the range of this list be, starting at 0?

#Out of Bounds
#Lists have an end to them, like an out of bounds line in the game of football; if we go out of bounds in football, we have left the field of play.
#Lists have this same sort of boundary; we can accidentally go past their end!
#What happens when we go past the end? Try uncommenting the next two lines of code
# things = ['hotdog', 3, 'apple', 1.2045313, ['a', 'b', 'c'], 'pizza']
# print(things[6])
#What happend?

#One way to prevent going out of bounds is knowling how long the list is. Here, we can use the len() function to help us out!
#Let's try it below:
# things = ['hotdog', 3, 'apple', 1.2045313, ['a', 'b', 'c'], 'pizza']
# print(f'The length of the list is {len(things)}')
# n = int(input('Pick a number between 1 and 6: '))
# print(things[n-1])

#More About Lists
#As you may have noticed, lists store data that exists between the square brackets, [].
#Every item in the list is separated by commas.
#We can print an item from a list using its index: print(animals[2])
#Lists can store more than one data type in them--including other lists!
#Lists should be considered a big box: sometimes there are other boxes within that box, ad infinitum.
#A list within a list is called a nested list

#Nested Lists
#Nested lists occur whenever a list contains another list
#Check out the nested list:
items = ['a', 'b', 'c', ['d', 'e']]
#How many elements are in this list? How could you quickly find out?
#What would be printed in the console if we ran the following line of code?
sublist = items[3]
print(sublist)
print(sublist[0])

#Tricky Stuff!
#We may have noticed that print(items[3]) output ['d', 'e'], but how would we print just 'd'?
#items = ['a', 'b', 'c', ['d', 'e']]