class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def setAge(self,newAge):
        if newAge<18:
            raise ValueError("Enter correct age..")
        self._age=newAge

person=Person("Jayanta",54)
person.setAge=45
print(person.name)
print(person.age)