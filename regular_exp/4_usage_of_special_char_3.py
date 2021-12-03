# {m} specifies that exactly m copies of previous RE should be matched.
# {m,n} causes resulting RE to match from m to n repetitions of previous RE.
# If m is omitted, it implies lower bound of zero.
# If n is omitted, upper bound is infinite.

import re
re.findall('a{2}', 'aaabcd')    # match a substring of 'aa'
#['aa']  
re.findall('.{1,3}', 'abbcccd') # match any substring of 1-3 characters
#['abb', 'ccc', 'd']

import re
regex_1 = '{4}'     #  match exactly 4 characters
regex_2 = '.{0,}'   #  match 0 or more characters
regex_3 = '.{0,1}'   #  match 0 or 1 character 
regex_4 = '.{1,}'   #  match 1 or more character 