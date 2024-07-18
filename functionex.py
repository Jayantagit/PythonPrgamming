def squareNum(num):
    return num*num
print(squareNum(4))

def addNums(num1,num2=7):
    return num1+num2
print(addNums(4))

def sum_sub(a,b):
    summation=a+b
    substraction=a-b
    return summation,substraction
print(sum_sub(5,1))
print("=============")
n=5
mat=[]
for i in range(5):
    mat.append([0]*n)
for r in range(n):
    mat[r][0]=1
    for c in range(1,r):
       mat[r][c]=mat[r-1][c]+mat[r-1][c-1]
    mat[r][r]=1
print(mat)
print("=============")
q=5
def fibo(n):
  if n<=1:
        return n
  return n*fibo(n-1)
print(fibo(5))
