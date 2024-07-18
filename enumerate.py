dict={"name":"Jayanta","age":30,"location":"Jodhpur"}
for k,v in dict.items():
    print(f"{k}  :{v}")
for val in set(dict.values()):
    print(f"and {val}")
print("=====================")
arr=[1,2,3,4,67]
for index,value in enumerate(arr):
    print(f"{index}  :{value}")
print("=====================")
p=lambda a,b,c:a+b+c
print(p(10,20,30))
print("=====================")
arr =[val for val in set(dict.values()) if val==30 or val=="Jayanta"]
print(arr)
print("=====================")
arr1=[10,20,30,40,65,80]
arr2=[i**2 for i in arr1 if i%2==0]#List Comprehension
print(arr2)
