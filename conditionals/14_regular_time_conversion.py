"""Write a function that converts the time from military to regular format."""

def time12hr(time):
    hh=int(time[:2])
    if(hh>12):
        hh-=12
        return str(hh)+":"+time[2:]+" p.m."
    elif(hh==12):
        return str(hh)+":"+time[2:]+" p.m."
    else:
        return str(hh)+":"+time[2:]+" a.m."

print(time12hr('1619'))
print(time12hr('1200'))
print(time12hr('1020'))