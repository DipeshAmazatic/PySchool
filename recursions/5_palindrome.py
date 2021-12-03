# A palindrome is a word, phrase, number or other sequence of units that can be read the same way in either 
# direction. Write a recursive function that determines whether the given word is a palindrome.

def isPalindrome(word):
    if(len(word) < 1):
        return True
    else:
        if(word[0].lower() == word[-1].lower()):
            return isPalindrome(word[1:-1])
        else:
            return False


print(isPalindrome("Racecar"))
print(isPalindrome("Never"))
print(isPalindrome("level"))