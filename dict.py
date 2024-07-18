dict={"name":"Jayanta","age":26,"schoool":"Patha Bhavan","gender":'M',"language":["Java","Python"],
     "empDetails": {"company":"LTI","id":"6108209"},("Kol","Bangalore"):"Home"}
#Key =Cannot give mutable ds=List,Dictionary
for key in dict.keys():
    print(key,"=",dict.get(key),"=",dict[key])

print(end="\n")
for key,value in dict.items():
    print(key,":",value)

print(end="\n")
#Update the Key
dict["age"]=53
print(dict)

print(end="\n")
for v in dict.values():
    print(v)
print(end="\n")

removeItem=dict.pop("age")
print(removeItem)
print(dict)

dict.pop('gender')
print(dict)



