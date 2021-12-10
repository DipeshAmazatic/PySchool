# A palindrome is a word, phrase, number or other sequence of units that can be read the same way in either 
# direction. Write a function that determines whether the given word or number is a palindrome.

def isPalindrome(word):
    if(len(str(word))>1):
        return str(word).lower()==str(word).lower()[::-1]
    return False


print(isPalindrome("Racecar"))
print(isPalindrome(121))
print(isPalindrome("Never"))
print(isPalindrome("level"))
print(isPalindrome(""))