list1=[1,2,3,True,"Jayanta"]
print(type(list1))

print("============")
#list2=eval(input("enter the list :"))
#print(list2)
#print(type(list2))
print("============")
list3=list(range(0,20,3))
print(list3)

print("============")
s="Sunita"
list4=list(s)
print(list4)
print("============")
s1="Jayanta Mandal"
list6=s1.split(" ")
print(list6)

print("============")
lang=["Java","Spring","Jmeter","Playwright","Cypress","ETL"]
print(lang[1:len(lang):2])
print(lang[::-1])
print(lang[-1::-2])
print("============")
for l in lang:
    print(l)
print("============")
x=0
n=len(lang)
while(x<n):
    print(lang[x])
    x=x+1