"""Making use of the 'break' statement to abort a for/while loop,
 and move to the code after the loop block ."""

 # insert 'break' in following code so that the comment
# after '#' (including '#') are stripped.
def stripComment(sentence):
    codeonly  = ""
    for ch in sentence:
        if ch == '#':
            break
        else:
	    #codeonly += '#'
            codeonly+=ch  
    return codeonly
print(stripComment('title = "Python in Action" # Initialize title'))