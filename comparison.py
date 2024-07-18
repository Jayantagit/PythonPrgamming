print(ord("A"))
s=" hi jay "
print(s.strip())

print("===============")
str="Hi Jayanta how are you Jayanta"
print("Find with ccorrect substring",str.find("Jayanta"))
print("Find with in ccorrect substring",str.find("Jayanta1")) #-1
print("Index with ccorrect substring",str.index("Jayanta"))
#print(str.index("jayanta")) #ValueError: substring not found
print("================")
print("Backward Find:",str.rfind("Jayanta"))
print("Backward Index:",str.rindex("Jayanta"))
print("jayanta" in str)
print("================")
print("Count in mainstring",str.count("Jayanta"))
print("Replace Method",str.replace("Jayanta","Manish"))
print(str)
print("================")
dt="22-08-1972"
list1=dt.split("-")
print(list1)
sep="/"
print("post joining",sep.join(list1))
print("================")
str1="bangAlore city"
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.swapcase())
print(str1.capitalize())
print(str1.startswith("bang"))
print(str1.endswith("city"))
print("================")
str2="priya786"
str33="189"
print(str2.isalpha())
print(str2.isalnum())
print(str33.isnumeric())
print(" ".isspace())
print("================")
str7="I live in bangalore and bangalore is in Karnakta and bangalore weather is good"
print(str7.find("bangalore",str7.find("bangalore")+1))
