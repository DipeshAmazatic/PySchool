# Write the function getVowels(word) that takes in a word as an argument and returns the vowels ('a', 'e', 'i', 'o', 'u') 
# in that word.


def getVowels(word):
    return [i for i in word if(i in ['a','e','i','o','u','A','E','I','O','U'])]

print(getVowels("apple"))
print(getVowels("Apple"))
print(getVowels("Banana"))