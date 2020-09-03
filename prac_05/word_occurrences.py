"""CP1404 - Practicals - prac_05
    Word Occurrences
"""

# example:
# word_to_count = {}
# text = input("Text: ")
# words = text.split()
#
# for word in words:
#     frequency = word_to_count.get(word, 0)
#     word_to_count[word] = frequency + 1
#
# words = list(word_to_count.keys())
# words.sort()
#
# max_length = max(len(word) for word in words)
# for word in words:
#     print("{:{}} : {}".format(word, max_length, word_to_count[word]))

# ----


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