word="jayanta"
d={}
for x in word:
   d[x]=d.get(x,0)+1
print(d)

for k,v in d.items():
    print(k,"=",v)
print("===============")
wordwithVowels="jayantae"
print(type(wordwithVowels))
vowels={"a","e","i","o","u"}
d1={}
for x in wordwithVowels:
   if x in  vowels:
     d1[x]=d1.get(x,0)+1
for k,v in d1.items():
    print(k,"=",v)
print("===============")
dictcompreheniosn={x:x*2 for x in range(5)}
print(dictcompreheniosn)
