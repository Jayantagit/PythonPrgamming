studDetails={"name":"Jayanta","rollno":1234,"address":"1234 Test Street"}
print(studDetails["rollno"])
d1={}
d2=dict()
d2["empno"]=122250
d2["desig"]="qa"
print(d2)
print("name" in studDetails.keys())
print(1234 in studDetails.values())
print(studDetails.get("address"))
print(studDetails.get("desig","QA Lead"))
print(studDetails.pop("address"))
print(studDetails)
for key in studDetails.keys():
    print(key,": ",studDetails[key])
print("===========")
for k,v in studDetails.items():
    print(k,v)
d2.update(studDetails)
print(d2)
print("===========Q1===========")
n=int(input("Enter no of Students:="))
d={}
for i in range(n):
    name=input("Enter name: =")
    mark = input("Enter mark: =")
    d[name]=mark
print(d)
try:
    while(True):
       nm=input("Enter name to show marks;")
       mark=d.get(nm,-1)
       if(mark!=-1):
          print(nm ,";",mark)
       else:
          opt=input("Do you want to try(y/n): ")
          if opt=="y":
              nm = input("Enter name to show marks;")
              mark = d.get(nm, -1)
              if (mark != -1):
                  print(nm, ";", mark)
                  break
          elif opt=="n" :
              break
          else:
              print("incorrect option..")
              break
except:
    pass
print("===========Q2===========")
dd=eval(input("enter the Dictionary :"))
print(sum(dd.values()))


