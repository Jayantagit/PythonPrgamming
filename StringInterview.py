#Reverse a string
s1="Kolkata"
s2=s1[::-1]
print(s2)
s3="Sunita"
print("".join(list(reversed(s3))))
print("".join(reversed(s3)))
print("===================")
s4="Bangalore"
rev=""
n1=len(s4)-1
while n1>=0:
    rev=rev+s4[n1]
    n1-=1
print(rev)
print("===================")
nm="Vikram Singh"
nmArr=nm.split(" ")
nmrev=""

for s in nmArr:
    nmrev=nmrev+"".join(reversed(s))+ " "
print(nmrev.strip())
l11=[]

for word in nmArr:
    l11.append(word[::-1])

print(" ".join(l11))
print("===================")
lang="Jmeter"
langeven=lang[0::2]
langodd=lang[1::2]
print(langeven)
print(langodd)
print("===================")
lang1="Selenium"
lang2="Java"
p,q=0,0
output=""
while p<len(lang1) or q<len(lang2):
    if p<len(lang1) :
        output=output+lang1[p]
    if q<len(lang2) :
        output=output+lang2[q]
    p=p+1
    q=q+1
if p>len(lang1):
    output=output+lang2[p:]
if q>len(lang2):
    output=output+lang1[q:]
print("output:=",output)
print("===================")
wordn="a4b2c3"
newoutput=""
count=0
for ch in wordn:
    if ch.isalpha():
        pass
    elif ch.isnumeric():
        newoutput=newoutput+wordn[count-1]*(int(ch))
    count=count+1
print(newoutput)
print("===================")
inpu1="a5b4c2"
output1=""
print(chr(97))
print(ord("a"))
for ch in inpu1:
    if ch.isalpha():
        x = ch
        output1=output1+ch
    else:
       output1+= chr(ord(x)+int(ch))
print(output1)


