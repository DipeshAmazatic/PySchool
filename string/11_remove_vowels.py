# Write the function removeVowels(word) that removes all the vowels ('a', 'e', 'i', 'o', 'u') in a 
# word and returns the remaining letters in the word

def removeVowels(word):
    #word=list(word)
    return ''.join([i for i in list(word) if(i not in ['a','e','i','o','u','A','E','I','O','U'])])
    # i=0
    # while(i<len(word)):
    #     if(word[i] in ['a','e','i','o','u','A','E','I','O','U']):
    #         word.remove(word[i])
    #     else:
    #         i+=1
    #return ''.join(word)
print(removeVowels('apple'))
print(removeVowels('Apple'))
print(removeVowels('Banana'))