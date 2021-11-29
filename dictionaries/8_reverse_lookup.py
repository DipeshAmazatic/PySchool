# Write a function reverseLookup(dictionary, value) that takes in a dictionary and a value as arguments and 
# returns a sorted list of all keys that contains the value. The function will return an empty list 

def reverseLookup(dictionary, value):
    return [i for i in dictionary if(dictionary[i]==value)]

print(reverseLookup({'a':1, 'b':2, 'c':2}, 1))
print(reverseLookup({'a':1, 'b':2, 'c':2}, 2))
print(reverseLookup({'a':1, 'b':2, 'c':2}, 3))