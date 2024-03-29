class Animal:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = Animal.count
        Animal.count += 1

    def display(self):
        print("Animal ", self.id, ":")
        print("\tName: : ", self.name)
        print("\tAge: : ", self.age)

a1 = Animal("Sharik", 5)
a2 = Animal("Muhtar", 13)

a1.display()
a2.display()