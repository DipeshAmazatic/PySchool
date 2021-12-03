# Write a function that validates an email address. For the sake of this exercise, a valid email address is 
# of the form <localname>@<domain>, where domain ends with .(dot) 'com', 'edu' or 'org'.

import re
def validate(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{3}\b'
    if(re.fullmatch(regex, email)):
        return "Valid Email"
 
    else:
        return "Invalid Email"


print(validate('john123@hotmail.com'))
print(validate('john.123@hotmail.com'))
print(validate('john123@gmail'))
print(validate('sa!!y@hotmail.com'))