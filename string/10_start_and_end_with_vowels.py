# Write the function startEndVowels(word) that returns True if the word starts and ends with vowel

def startEndVowels(word):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    return (word.startswith(vowels) and word.endswith(vowels))


print(startEndVowels('apple'))
print(startEndVowels('google'))
print(startEndVowels('A'))
print(startEndVowels(''))