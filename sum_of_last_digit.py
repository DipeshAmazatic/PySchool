##  1st Method
def getSumOfLastDigits(list1):
    sum1=0
    for i in list1:
        sum1+=int(str(i)[len(str(i))-1])
    return sum1

#print(getSumOfLastDigits([1,21,33,1234,54,1,45]))

## 2nd Method
def detsum(di):
    return int(str(di)[len(str(di))-1])
print(sum(list(map(detsum,[1,21,33,1234,54,1,45]))))
