# Write the function startWithVowel(word) that takes in a word as argument and returns a substring that 
# starts with the first vowel found in the word. The function returns 'No vowel' if the word does not contain vowel.

def startWithVowel(word):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    for index,char in enumerate(word):
        if(char in vowels):
            return word[index:]
    return "No vowel"

print(startWithVowel('apple'))
print(startWithVowel('google'))
print(startWithVowel('xyz'))