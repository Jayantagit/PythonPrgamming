
def findDiff(nums):
    n=len(nums)
    expected_sum=n*(n+1)//2
    actual_sum=sum(nums)
    return expected_sum-actual_sum
print(findDiff([0,1,3,4,5,6,7,8]))