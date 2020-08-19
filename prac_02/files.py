"""
CP1404 Practicals - prac_02
Files
"""

# 1.
out_file = open('data.txt.', 'w')
user_name = input("Enter name: ")
print(user_name, file=out_file)
out_file.close()

# 2.
out_file = open('data.txt', 'r')
user_name = out_file.readline()
print("Your name is {}".format(user_name))
out_file.close()

# 3.
out_file = open('numbers.txt', 'r')

numbers_to_add = out_file.readlines()

first_number = int(numbers_to_add[0])
second_number = int(numbers_to_add[1])

total = first_number + second_number

print("Total = {}".format(total))
out_file.close()

# 4.
out_file = open('numbers.txt', 'r')

contents = out_file.readlines()
numbers_of_lines = len(contents)
line_number = 1

for x in range(numbers_of_lines):
    current_contents = contents[x]
    print("Contents of numbers.txt at line {}: {}".format(line_number, current_contents))
    line_number += 1

out_file.close()
