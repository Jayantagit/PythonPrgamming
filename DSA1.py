from functools import reduce
l1=[1,2,2,4,5,6]
s1=set(l1)
print(s1)
orig_sum=reduce(lambda x,y:x+y ,s1)
unique_sum=reduce(lambda x,y:x+y ,l1)
print("Repeating element:",unique_sum-orig_sum)
for p in range(1,7):
    if p not in s1:
        print("Missingelement:", p)
        break
print("======================")
listnum=[1,2,3,5]
def missing_num(nums):
    n=len(nums)
    xor=0
    for i in range(1,n+2):
        xor ^= i
    print(xor)
    for i in range(n):
        xor ^= nums[i]
    return xor
print(missing_num(listnum))
print("======================")
listnum=[1,2,3,5.3]
def missing_repeatingnum(nums):
    n=len(nums)
    exp_sum=n*(n+1)//2
    exp_square=n*(n+1)*(2*n+1)//6
    actual_sum=0
    actual_square=0
    for i in range(n):
        actual_sum+=nums[i]
        actual_square += nums[i]*nums[i]
    print("Missing num",(exp_sum-actual_sum))
missing_repeatingnum(listnum)
print("======================")
k=[1,3,4,2,2]
dic={}
for item in k:
    if item in dic.keys():
        dic[item] = dic.get(item)+1
    else:
        dic[item]=1

print(dic)
for key,val in dic.items():
    if val>1:
        print("Duplicate val: ",key)
print("======================")
#Floyd Cylcic detection
def dup_numbers(nums):
    slow=fast=nums[0]
    #Meeting Point
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break
    slow =nums[0]
    #Entry point
    while slow!=fast:
        slow=nums[slow]
        fast=nums[fast]
    return fast
print(dup_numbers(k))
print("======================")
list77=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
row=len(list77) #row
col=len(list77[0]) #col
low=0
high=(row*col)-1
print(row,low,high)
target=16
rownum , colnum=0 ,0
while low<high:
    mid=low+(high-low)//2
    r=mid//col
    c=mid%col
    midElement=list77[r][c]
    if midElement==target:
        rownum,colnum=r,c
        break
    elif  midElement>target:
        high=mid-1
    else:
        low=mid+1
print(rownum,colnum)



