#Lab 2.03 Solution
import math

#Task 3: Create!
#In the space below, your job is to make a program that analyzes information about a triangle.
#The program will be able to do the following:
#1. The program will ask for 3 side lengths from the user
#2. The program will determine, based on the side lengths, what kind of triangle it is (scalene, isosceles, equilateral)
#3. The program will determine, based on the side lengths, whether it is a triangle or not (consider the triangle inequality theorem)
#4. The program will determine, based on the side lengths, the perimeter of the triangle
lengths = []
a = int(input('What is the first side length? '))
lengths.append(a)
b = int(input('What is the second side length? '))
lengths.append(b)
c = int(input('What is the third side length? '))
lengths.append(c)
# print(lengths)
lengths.sort()
print(lengths)

perimeter = lengths[0] + lengths[1] + lengths[2]
if lengths[0] + lengths[1] >= lengths[2]:
    if lengths[0] == lengths[1] == lengths[2]:
        h = (lengths[0]*(math.sqrt(3)))/2
        area = 0.5 * lengths[0] * h
        print('Your triangle is equilateral')
    elif (lengths[0] == lengths[1]) or (lengths[0] == lengths[2]) or (lengths[1] == lengths[2]):
        h = (math.sqrt(lengths[0]**2 - (lengths[0]/2)**2))
        area = 0.5 * lengths[0] * h
        print('Your triangle is isosceles')
    else:
        angleC = math.acos((lengths[2]**2 - lengths[1]**2 - lengths[0]**2)/(-2*lengths[0]*lengths[1]))
        # angleC = math.degrees(angleC)
        print(angleC)
        angleB = math.asin((lengths[1] * (math.sin(angleC)))/(lengths[2]))
        print(math.degrees(angleB))
        h = (lengths[0]) * (math.sin(angleB))
        print(h)
        area = 0.5 * h * lengths[2]
        print('Your triangle is scalene')
    print(f'The perimeter of your triangle is {perimeter}')
    print(f'The area of your triangle is {area}')
else:
    print('You don\'t have a triangle')