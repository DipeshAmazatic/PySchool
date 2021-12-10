# Write a function countLetters(word) that takes in a word as argument and returns a list of tuples that 
# shows the number of times each letter appears. The letters must be sorted in alphabetical order.
from collections import Counter
def countLetters(word):
    return Counter(word)


print(countLetters('google'))
print(countLetters('apple'))
print(countLetters('microsoft'))