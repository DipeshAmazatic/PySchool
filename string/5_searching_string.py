# Write the function search(word, substring) that takes in a word and a substring as arguments and 
# returns the position (0 indexed) of the substring if it is found in the word. The function returns -1 
# if the substring is not found.


def search(word, substring):
    return word.find(substring)

print(search("apple", 'p'))
print(search("google", 'apple'))
print(search("google", 'p'))
print(search("google", 'oo'))