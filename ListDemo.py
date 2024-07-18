demo=["jayanta",53,"JU",True,87.98,[1,2,3,4,5],("Mango","Jam")]
print(demo)
print(type(demo))
print(demo[2])
demo[4]=99.99
print(demo)
for l in demo:
    print(l,end=" ")

print("",end="\n ")
demo.append({"id":"1140960"})
print(demo)
print("",end="\n ")
print(demo[3:5])
print(demo[-1::-1])
demo.insert(1,"MT")
print(demo)
print(len(demo))
demo.remove("jayanta")
print(demo)
print("",end="\n ")
course="Metallurgy"
print(list(course))
"""
delete a list
"""
demo.extend([89,98,"Patha Bhavan"])
print(demo)
studata=[1,2,3,4,5]
studata[1:3]=["Jay","Tom"]
print(studata)
del studata[2:4]
print(studata)
studata.clear()
print(studata)
studata1=[1,2,3,4,5]
print(studata1.pop(4))
print(studata1)