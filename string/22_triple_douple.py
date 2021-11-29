# Write a function isTripleDouble(word) that takes in a word as argument and returns True if the word 
# contains three consecutive double letters.

def isTripleDouble(word):
    i=0
    while(i<len(word)-5):
        if(word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]):
            return True
        i+=1
    return False

print(isTripleDouble('appllee'))
print(isTripleDouble('aapplee'))
print(isTripleDouble('applle'))