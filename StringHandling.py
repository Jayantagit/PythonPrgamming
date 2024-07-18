str="Welcome"
print(str[-1::-1])
print(str[0:len(str)])

i=0
for c in str:
    print(c,"Present in index :",i,"reverse index",i-len(str))
    i=i+1
print("=============")
s="Learning Python is easy"
print(s[0:len(s)+1:2])
print(s[::-1])
print(s[:7])
print(s[-7:9:-1])
print(s[-7:-(len(s)+1):-1])
print("=============")
print(s+" Isha")
print(s*2)
print("=============")
i=0
n=len(s)-1
while i<=n:
    print(s[i])
    i=i+1
print("=============")
j=-1
n=-(len(s)+1)
while j>=n:
    print(s[j])
    j=j-1