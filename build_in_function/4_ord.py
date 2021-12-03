# ord(c) Return the ASCII code of a character. ord is the opposite of chr.

# Write a function that capitalizes the first character of each word.
def capitalize(phrase): 
    result=''
    for i in phrase.split(' '):
        result+=chr(ord(i[0])-32)+i[1:]+' '
    return result

print(capitalize('how are you?'))