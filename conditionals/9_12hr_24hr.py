"""Write a function that converts the time to 24hr format."""
def time24hr(tstr):
    last_two=tstr[-2:]
    hh=int(tstr[:2])
    if(last_two=='am'):
        if(hh==12):
            hh=00
        elif(hh>12):
            hh=hh-12
        return str(hh)+tstr[3:5]+'hr'
    else:
        return str(hh)+tstr[3:5]+'hr'

print(time24hr('12:34am'))
print(time24hr('12:15pm'))