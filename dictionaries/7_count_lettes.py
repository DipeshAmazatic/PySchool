# Write a function countLetters(word) that takes in a word as argument and returns a dictionary 
# that counts the number of times each letter appears.

def countLetters(word):
    letters_count={}
    for i in word:
        if(i in letters_count):
            letters_count[i]+=1
        else:
            letters_count[i]=1
    return letters_count

print(countLetters('google'))
print(countLetters('apple'))
print(countLetters(''))