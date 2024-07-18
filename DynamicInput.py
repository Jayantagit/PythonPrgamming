a=int(input("Enter the num1:="))
b=int(input("Enter the num2:="))
print(a+b)
#Conditional stmt
if a%2==0 and b%2==0:
    print("even numbers")
else:
    print("odd num")

mark=int(input("Enter the mark="))

if mark>90:
    grade="A"
elif mark>70 and mark<=90:
    grade="B"
else:
    grade="C"
print("Grade is :="+grade)
