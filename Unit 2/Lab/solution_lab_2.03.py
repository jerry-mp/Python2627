#Lab 2.03 Solution

#Task 3: Create!
#In the space below, your job is to make a program that analyzes information about a triangle.
#The program will be able to do the following:
#1. The program will ask for 3 side lengths from the user
#2. The program will determine, based on the side lengths, what kind of triangle it is (scalene, isosceles, equilateral)
#3. The program will determine, based on the side lengths, whether it is a triangle or not (consider the triangle inequality theorem)
#4. The program will determine, based on the side lengths, the perimeter of the triangle
a = int(input('What is the first side length? '))
b = int(input('What is the second side length? '))
c = int(input('What is the third side length? '))
perimeter = a + b + c
if a + b >= c:
    if a == b == c:
        print('Your triangle is equilateral')
    elif (a == b) or (a == c) or (b == c):
        print('Your triangle is isosceles')
    else:
        print('Your triangle is scalene')
    print(f'The perimeter of your triangle is {perimeter}')
else:
    print('You don\'t have a triangle')

a = 3
b = 4
c = 5

if not ((a + b > c) and (b + c > a) and (a + c > b)):
    print('not a triangle')
elif a == b == c:
    print('equal')
elif a == b or a == c or b == c:
    print('isosceles')
else:
    print('scalene')
