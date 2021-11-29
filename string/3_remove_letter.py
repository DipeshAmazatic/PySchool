# Write a function removeLetter(word, letter) that takes in a word and a letter as arguments and 
# remove all the occurrence of that particular letter from the word. The function will returns the 
# remaining leters in the word.

def removeLetter(word, letter):
    word = list(word)
    for i in range(word.count(letter)):
        word.remove(letter)
    return ''.join(word)


print(removeLetter("apple", "p"))
print(removeLetter("microsoft", "o"))
print(removeLetter("google", "g"))