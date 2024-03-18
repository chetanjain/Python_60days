"""
Your task is to create a program that generates a random whole number.
Here is how the program should behave:
"""
import random

lower_bound = int(input("Enter the lower bound : "))
upper_bound = int(input("Enter the upper bound : "))

random_number = random.randrange(lower_bound,upper_bound)
print(random_number)

