"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
typ_pi = type(pi)
print(pi,typ_pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i<50:
    print("Less than 50")
elif i>50:
    print("Greater than 50")
else:
    print("Equal with 50")
print(i)

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print("The fruit is orange")
elif picked_fruit == 'strawberry':
    print("The fruit is red")
else:
    print("The fruit is yellow")

print(picked_fruit)
# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiple_numbers(A,B):
    result=A*B
    return result

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", multiple_numbers(12,96))

print("48 x 17 =", multiple_numbers(48,17))

print("196523 x 87323 =", multiple_numbers(196523, 87323))
