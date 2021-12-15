"""Create a function genSet() that takes in a list of numbers and returns a sorted set."""
def genSet(nums):
    nums=list(set(nums))
    nums.sort()
    return nums
print(genSet([5,4,8,4,9,8]))
print(genSet([3,-2,-1,-1,3,-2,0]))