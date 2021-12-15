"""Write a function to convert temperature from Celsius to Fahrenheit scale.
oC to oF Conversion: Multipy by 9, then divide by 5, then add 32."""
# Note: Return a string of 2 decimal places.
def Cel2Fah(temp):
    """convert cel to fah"""
    return temp * (9 / 5) + 32

print("%.2f"%Cel2Fah(28.0))
print("%.2f"%Cel2Fah(0.00))