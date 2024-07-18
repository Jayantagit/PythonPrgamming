def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

for i in range(5):
       print(recur_fibo(i))

def printNum(listVal,si):
     if(si>=len(listVal)):
         return;
     printNum(listVal, si+1)
     print(listVal[si])

printNum([6,8,7,5],0)
