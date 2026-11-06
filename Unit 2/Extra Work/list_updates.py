#List Updates

#Objective
#The purpose of this activity is to practice the ability of updating data found in a list!

#Data in a list requires us to do a reassignment, that is, to actually update the data found within a given index.

#First, we will look at the simple updating of a list via a simple array, and second, we will look at a more complex array

#Example 1
#Uncomment the list below:
# foods = ['hot dog', 'apple', 'pasta', 'chicken and rice', 'popcorn', 'chocolate']
#Task 1: Update the list by adding an additional food item to the list
# foods.append('yams')
# print(foods)
#Task 2: Update the list by changing an item in the list
# foods[0] = 'yams'
# print(foods)

#Task 3: Update the list by adding additional details to an item in the list
# foods[4] = foods[4] + ' and butter'
# print(foods)

#Example 2:
#Uncomment the array below:
closet = [
    #Shirts
    ['t-shirt', 'blouse', 'sweatshirt'],
    #Pants
    ['jeans', 'shorts', 'gym shorts'],
    #Shoes
    ['dress shoes', 'sneakers', 'loafers']
]

#Task 1: Print out an item found in the Shirt section
print(closet[0][1])
#Task 2: Print out an item found in the Pants section
print(closet[1][2])
#Task 3: Print out an item found in the Shoes section
print(closet[2][2])
#Task 4: Update and change an item found in the Pants section
closet[1][1] = 'sweatpants'
print(closet[1])
#Task 5: Change up to three items in the Closet; then, print out the updated Closet
closet[0][1] = 'tank top'
closet[2][1] = 'high heels'
print(closet)