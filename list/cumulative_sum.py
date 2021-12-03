# Write a function calCumulativeSum(numbers) that takes in a list of numbers as argument and returns the 
# cumulative sum of the list. That is, the new list where the i element is the sum of the first i + 1 elements 
# from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].

def calCumulativeSum(numbers):
    for i,val in enumerate(numbers):
        if(i!=0):
            numbers[i]=numbers[i-1]+numbers[i]
    return numbers

print(calCumulativeSum([1,2,3]))
print(calCumulativeSum([2,2,2]))
print(calCumulativeSum([2,4,6]))