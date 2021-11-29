# Write a function isInAlphabeticalOrder(word) that takes in a word as argument and returns True if the word contains 
# letters that are arranged in alphabetical order. For example, the letter 'c' should not appear before the letter 'a'.


def isInAlphabeticalOrder(word):
    base=word[0]
    for i in range(1,len(word)):
        if(word[i]>=base):
            base=word[i]
        else:
            return False
    return True

print(isInAlphabeticalOrder('app'))
print(isInAlphabeticalOrder('apple'))
print(isInAlphabeticalOrder('goo'))
print(isInAlphabeticalOrder('google'))