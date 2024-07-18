s="Jayanta Mandal"
nm=s.split(" ")
for n in nm:
    print(n)
print(s[len(s)-1])
print(s[-1])
print(s[1:7])
print("=========")
pname="Mindtree"
print(pname[-7:9])
print(pname[-1:-7:-1])
print(pname[1:len(pname)+1:2])
print(pname[-1::-1])
print(pname[::-1])
print(pname[len(pname):2:-1])
print("========================")
print(f"Company name is {pname}")#f-string
print ("Compnany name is %s" %pname)
print ("Compnany name is {0}".format(pname))
print(pname.upper())
print(pname.title())
print(pname*2)
print(pname.replace("M","Y"))
print("tree" in pname)#Membership Operator