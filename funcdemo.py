from functools import reduce
def sub(a,b):
    return (a-b)
print(sub(b=10,a=8))

def sub1(p,q=10):
    return (p-q)

print(sub1(4))

def wish(msg,name="Sunita",surname="Singh"):
    print (msg,name,surname)
wish("Hi ")

def summation(*args):
    total=0
    for i in args:
        total+=i
    return total
print(summation(1,2,3,4,5))

print("==============")
v=5
def f1():
    global v
    v=10
    print(v)

def f2():
    print(v)
f1()
f2()
print("==============")
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
print(fact(5))
print("==============")
res=lambda x:x*x
print(res(5))
print("==============")
greater=lambda a,b:a if a>b else b
print(greater(10,20))
print("==============")
list2=[10,20,30,40]
def isEven(num):
    if num%2==0:
        return True
    else:
       return False

print(list(filter(isEven,list2)))
print(list(filter(lambda x:x%2==0,list2)))
print(list(map(lambda x:x*2,list2)))
print("==============")
l11=[1,2,3,4,5]
l22=[4,5,6,7,8]
print(list(map(lambda x,y:x+y,l11,l22)))
print("==============")
l6=[10,20,30,40,50]
print(reduce(lambda x,y:x+y,l6))
print("==============")
def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()
