"""Write a function using 'if/elif/else' conditionals to compute the BMI of a person,
and return the risk associated with cardiovascular diseases.

BMI = weight(kg)/( height(m)*height(m) )"""
def HealthScreen(weight, height):
    bmi=round(weight/(height*height),1)
    if(bmi>=27.5):
        return 'Your BMI is %s (High Risk).'%bmi
    elif(bmi>=23.0 and bmi<=27.4):
        return 'Your BMI is %s (Moderate Risk).'%bmi
    elif(bmi>=18.5 and bmi<=22.9):
        return 'Your BMI is %s (Low Risk).'%bmi
    else:
        return 'Your BMI is %s (Risk of nutritional deficiency diseases).'%bmi

print(HealthScreen(85, 1.75))
print(HealthScreen(68, 1.65))
print(HealthScreen(60, 1.63))
print(HealthScreen(40,1.58))