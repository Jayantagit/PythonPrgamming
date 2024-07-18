n=[10,20,30,40,60,10]
print(len(n))
print(n.count(10))
print(n.index(10))
n.extend(["Jayanta","male"])
print(n)

print("Jayanta" in n)

n.append(["LTI","QA"])
print(n)

print("=======================")
listnum=[]
for i in range(0,101):
    if i%10==0:
        listnum.append(i)
print(listnum)
print("=======================")
a1=[1,2,3,4,5,6]
a1.insert(2,22)
a1.insert(10,200)
a1.insert(-10,100)
print(a1)
print("=======================")
l11=["Chicken","Muton","Fisg"]
l22=["banana","pupkin"]
l11.extend(l22)
print(l11)
print("=======================")
l33=[30,40,50,60,70,30,120]
l33.remove(30)
print(l33)
pop1=l33.pop()
print(pop1 ,l33)
print(l33.pop(2))