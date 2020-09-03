numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9] (from 0 - the second last number)
# numbers[3:4] = [1, 5]
# 5 in numbers = numbers[4]
# 7 in numbers = There isn't any
# "3" in numbers = numbers[0]
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])

if 9 in numbers:
    print("Yes")
else:
    print("No")
