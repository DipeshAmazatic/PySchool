# Write a function that validates the password. It should be 6-8 characters long. It consists of alphanumeric 
# characters with a mixture of digits and letters.

import re
def validate(passwd):
    if(any(char.isdigit() for char in passwd)):
        if(re.fullmatch(r'[A-Za-z0-9]{6,8}', passwd)):
            return "Valid password."
        else:
            return "Invalid password"
    else:
        return "Invalid password"

print(validate('1234'))
print(validate('google'))
print(validate('passwd123'))
print(validate('passwd12'))
print(validate('pas@wd12'))