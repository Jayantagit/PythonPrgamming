set1={10,20,70,4,90,109}

print(set1)
print(type(set1))

list1=[10,20,30,40]
s=set(list1)
print(type(s))
print(s)
s2={}
print(type(s2))
print("========methods===========")
set2={10,20,70,4,90,109,120,189,90}
set2.add(567)
print(set2)
set2.update([0,1,3])
print(set2)
set2.remove(90)
print(set2)
set3=set2.copy()
print(set3)
set3.pop()
print(set3)
set3.discard(109)
print(set3)
set3.discard(199)#Will not throw any Key Error
print(set3)
print("========methods===========")
set11={1,2,3,4,10}
set22={2,3,4,5,6,7}
set33=set11.union(set22)
set44=set11.intersection(set22)
set55=set11.symmetric_difference(set22)
set66=set11.difference(set22)
print(set33)
print(set44)
print(set55)
print(set66)
#{expression for item in sequence if condition}//Set Comprehension
yy={x*x for x in set55 if x%2==0}
print(yy)

print("=====================")
kk=[1,2,2,4,7,8,9,8]
ll=[]
for item in kk:
    if item not in ll:
        ll.append(item)
print(ll)
