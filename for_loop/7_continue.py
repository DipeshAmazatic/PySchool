"""Making use of the 'continue' statement to skip the rest of execution within a loop 
block for current iteration, and move to the next iteration.
"""

# Insert 'continue' in following code so that it returns a
# string with no vowels.
def skipVowels(word):
    novowels = ''
    for ch in word:
        if ch.lower() in 'aeiou':
            continue
        else:
            novowels += ch
    return novowels

print(skipVowels('Hello'))