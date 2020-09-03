"""
CP1404 Practical - Prac_04
List exercises
"""

entered_numbers = []
number_of_numbers = 0

while number_of_numbers < 5:
    user_input = int(input("Enter a number: "))
    entered_numbers.append(user_input)
    number_of_numbers += 1

print("The first number is {}".format(entered_numbers[0]))
print("The last number is {}".format(entered_numbers[-1]))

sorted_numbers = sorted(entered_numbers)

print("The smallest number is {}".format(sorted_numbers[0]))
print("The largest number is {}".format(sorted_numbers[-1]))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input_name = input("Enter username: ")

if user_input_name in usernames:
    print("Access Granted")
else:
    print("Access Denied")
