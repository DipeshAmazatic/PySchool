# match(pattern, string[, flags])
# "match" is similar to "search", but it only returns a MatchObject if the pattern matches the beginning of the string.

import re
regex = r"^[a-zA-Z0-9]{4}"

print(re.search(regex, 'a123').group())
#('a123')
print(re.search(regex, 'zb42a').group())
#('zb42')