class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def bark(self):
        print("BARK BARK BARK")


if __name__ == '__main__':
    Animal = Animal("Animal", 29)
    print(Animal.getName())
    print(Animal.getAge())
    try:
        print(Animal.bark())
    except Exception as e:
        print(e)

    Doug = Dog("Doug", 29)

    print(Doug.getName())
    print(Doug.getAge())
    print(Doug.bark())
