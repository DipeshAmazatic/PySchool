# Write a function rightJustify(word) that takes in a word as argument and return a word with 
# leading spaces so that the last letter of the word is in column 50 of the display.

def rightJustify(word):
    return " "*(50-len(word))+word

print(rightJustify('apple'))
print(rightJustify('google'))
print(rightJustify('microsoft'))