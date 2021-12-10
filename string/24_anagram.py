# An anagram is a word formed by reordering the letters of another word. Write a function isAnagram(w1, w2) that 
# takes in two words as arguments and return True if one word is an anagram of the other word.


def isAnagram(w1, w2):
    w2=list(w2.lower())
    for i in w1.lower():
        if(i in w2):
            w2.remove(i)
        else:
            return False
    return True



print(isAnagram('google', 'gogole'))
print(isAnagram('google', 'gogoll'))
print(isAnagram('google', 'gogogo'))
print(isAnagram('Google', 'google'))