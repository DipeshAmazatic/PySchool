# Write the function capitalizeVowels(word) that returns the word with all the vowels capitalized.

def capitalizeVowels(word):
    for i in word:
        if(i in ['a','e','i','o','u']):
            word=word.replace(i,i.upper())
    return word

print(capitalizeVowels('apple'))
print(capitalizeVowels('google'))