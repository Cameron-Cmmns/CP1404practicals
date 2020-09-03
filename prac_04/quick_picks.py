"""
CP1404 - Practicals - Prac_04
"Quick Pick" Lottery
"""
import random

NUMBER_OF_RANDS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

random_number_list = []

number_of_picks = int(input("How many quick picks? "))

for x in range(number_of_picks):
    for y in range(0, NUMBER_OF_RANDS):
        random_number = int(random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER))
        print(random_number, end=" ")
    print("\n")
