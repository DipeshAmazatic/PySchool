# Write the function changeCase(word) that changes the case of all the letters in a word and returns the new word.


def changeCase(word):
    #word=list(word)
    #for index,i in enumerate(word):
    for i in word:
        if(i>='a' and i<='z'):
            word=word.replace(i,i.upper())
        else:
            word=word.replace(i,i.lower())
    #return ''.join(word)
    return word

print(changeCase('aPPle'))
print(changeCase('BaNaNa'))