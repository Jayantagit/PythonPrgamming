def mul(n,m):
    return n*m;

def add():
    return a+b;
a=3
b=7;
print(add())

class Car:
    no_cars=0
    def __init__(self,name):
        self.name=name
        self.update()

    @classmethod
    def update(cls):
        cls.no_cars += 1

    @classmethod
    def display(cls):
        print("Total cars created :",cls.no_cars)

c1=Car("a1")
c2=Car("a2")
c2=Car("a3")
Car.display()

if __name__=="__main__":
    print(mul(7,8))

