"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        input_integer = int(input("Enter an integer: "))
        result = input_integer
        finished = True
    except ValueError:
        print("Please enter a valid integer.")

# It is unclear if this is an example of a valid result;
# or if this is printing the valid result that has been entered.
print("Valid result is:", result)
