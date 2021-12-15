"""Write a function that uses a default value."""
def introduce(name, age=0):
    msg = "My name is %s. " % name
    if age == 0:
       msg += "I am %s years old."%age
    else:
       msg += "I am %s years old."%age
    return msg
print(introduce('Lim', 20))
print(introduce('Ahmad'))