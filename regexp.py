import re
text = "My phone number is 123-234-2655. call soon!"
patt='\d{3}-\d{3}-\d{4,}'
resul=re.search(patt,text)
print(resul.group())