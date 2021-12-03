# Write the function getCommonLetters(word1, word2) that takes in two words as arguments and returns a new 
# string that contains letters found in both string. Ignore repeated letters and sort the result in alphabetical order.

def getCommonLetters(word1, word2):
    return ''.join([i for i in set(word1) if(i in set(word2))])

print(getCommonLetters('apple','google'))
print(getCommonLetters('microsoft','apple'))
print(getCommonLetters('microsoft','google'))