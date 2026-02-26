# math.py

import math
import random

# Example 1: Built-in math functions
numbers = [4, -7, 15, 2]
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Absolute:", abs(-10))
print("Power:", pow(2, 3))


# Example 2: math module functions
print("Square root:", math.sqrt(25))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.7))
print("Pi value:", math.pi)


# Example 3: Trigonometric functions
angle = math.pi / 2
print("Sin:", math.sin(angle))
print("Cos:", math.cos(angle))


# Example 4: Random number generation
print("Random float:", random.random())
print("Random integer:", random.randint(1, 100))


# Example 5: Random choice and shuffle
colors = ["red", "blue", "green", "yellow"]

print("Random choice:", random.choice(colors))

random.shuffle(colors)
print("Shuffled list:", colors)