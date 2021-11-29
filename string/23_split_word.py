# Write a function splitWord(word, numOfChar) that takes in a word and a number as arguments. The function will 
# split the word into smaller segments with each segment containing the number of letter specified in the numOfChar 
# argument. These segments are stored and returned in a list.

def splitWord(word, numOfChar):
    splitWords=[]
    i=0
    while(i<len(word)):
        splitWords.append(word[i:i+numOfChar])
        i+=numOfChar
    return splitWords

print(splitWord('google', 2))
print(splitWord('google', 3))
print(splitWord('apple', 1))
print(splitWord('apple', 4))