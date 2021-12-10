# Write the function isReverse(word1, word2) that takes two words as arguments and returns True is 
# the second word is the reverse of the first word

def isReverse(word1, word2):
    return word1==word2[::-1]

print(isReverse('apple', 'elppa'))
print(isReverse('google', 'apple'))
print(isReverse('google', 'elgoog'))
print(isReverse('apple', 'alppe'))