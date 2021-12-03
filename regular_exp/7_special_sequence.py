# # \d matches any decimal digit.
# \D matches any non-digit character.

import re
re.findall('\d', '1a2b3c')
#['1', '2', '3']  
re.findall('\D', '1a2b3c')
#['a', 'b', 'c']

# What of the following statements regarding RE is false?

# '\d+' is equivalent to '[0-9+]'.