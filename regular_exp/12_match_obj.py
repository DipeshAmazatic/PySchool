# Fill in arbitrary value to the string so that mobj.span(2) returns (5, 7).
import re
mobj = re.search('(\d+)/(\d+)', 'Using pi=22/7, compute ...') # gets numerator and denominator
mobj.groups()
print(mobj)
string = 'Using2/7, compute ...'
mobj = re.search('(\d+)/(\d+)', string) 
print(mobj)