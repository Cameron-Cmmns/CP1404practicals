"""CP1404 - Practicals - prac_05
    Word Occurrences
"""

# Doesn't work: The count goes up for repeated words but they cannot be
# called based on the count inside the for loop.
# Possible Fixes: ##TO DO##

word_dict = {}

input_to_dict = input("Text: ")

words = input_to_dict.split()

count = 1

for x in range(0, len(words)):

    if words[x] == words[x - 1]:
        if x == 0 and words[x + 1] == words[x]:
            word_dict[words[x]] = count
            count += 1
        word_dict[words[x]] = count
        count += 1
    else:
        word_dict[words[x]] = 0

    x += 1

print(words)

print("")
