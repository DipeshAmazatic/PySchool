# Write a function countVowels(word) that takes in a word as an argument and returns the number of vowels ('a', 'e', 'i', 'o', 'u') in the word.

def countVowels(word):
    return len([i for i in word if(i in ['a','e','i','o','u','A','E','I','O','U'])])


print(countVowels('apple'))
print(countVowels('microsoft'))
print(countVowels('google'))