# Write the function countLetter(word, letter) that takes in a word and a letter as arguments 
# and returns the number of occurrence of that letter in the word.

def countLetter(word, letter):
    return word.count(letter)

print(countLetter("apple", "p"))
print(countLetter("Apple", "a"))
print(countLetter("Banana", "n"))