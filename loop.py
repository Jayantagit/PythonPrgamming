k=0
while k<10:
    print(k)
    k=k+1
print("done==")
for k in list(range(10,0,-1)):
    print(k)
print("done==")
for nm in ("jayanta","Ram","Manish"):
    if nm=="Ram":
        break
    print(nm);
for nm in ("jayanta","Ram","Manish"):
    if nm=="Ram":
        continue
    print(nm);
print("pass stmt==")
for nm in ("jayanta","Ram","Manish"):
   pass