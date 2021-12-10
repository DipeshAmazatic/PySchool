# Write a function isAllLettersUsed(word, required) that takes in a word as the first argument and returns True if 
# the word contains all the letters found in the second argument.


def isAllLettersUsed(word, required):
    for i in required:
        if(i in word):
            continue
        else:
            return False
    return True

print(isAllLettersUsed('apple', 'apple'))
print(isAllLettersUsed('apple', 'google'))
print(isAllLettersUsed('learning python', 'google'))
print(isAllLettersUsed('learning python', 'apple'))