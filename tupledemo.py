tup=("jay","Manish","roy","Peter","Kumar",12,["122201","Somnath"])
print(tup[1:3])
#tup[0]="Jayanta"
print(tup)
print(tup[6][1])
for p in tup:
    print(p,end="")
tup1=tuple([1,2,3,4,5])
print(tup1)
print("=============")
a,b,c=(10,11,12)#unpacking
print(c,b)
pack=10,40,78
print(type(pack))#packing
print(pack)
print("=============")
#del tup[0]
del tup
print(tup)