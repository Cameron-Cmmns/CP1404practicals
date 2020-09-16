"""CP1404 - Practicals - prac_05
    Word Occurrences
"""


# Large portion copied off the example; previous attempts didn't work.
# had to use the example for this.
word_dict = {}
input_to_dict = input("Text: ")
words = input_to_dict.split()

for word in words:
    word_frequency = word_dict.get(word, 0)
    word_dict[word] = word_frequency + 1

words = list(word_dict.keys())
words.sort()

max_length = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, max_length, word_dict[word]))