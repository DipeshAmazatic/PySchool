"""Write a function to compute the BMI of a person.
BMI = weight(kg)  /  ( height(m)*height(m) )"""
# Note: Return a string of 1 decimal place.
def BMI(weight, height):
    return weight / (height *height)
print("%.2f"%BMI(63, 1.7))
print("%.2f"%BMI(110, 2))