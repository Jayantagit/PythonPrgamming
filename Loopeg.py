for x in range(6):
    if x==4:
        break
    print(x)

print("==============")
cart=[100,200,300,500,800,170]
for item in cart:
    if item>300:
        continue
    print(item)
else:
    print("all items processed successfully")
print("==============")
def m1():
    pass
    print("m1")
m1()
print("==============")
a=90
del a
#print(a)
b=89
b=None
print(b)