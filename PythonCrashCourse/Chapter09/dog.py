class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('xiaobuding', 6)
you_dog = Dog('guaiguai', 7)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + " years old.")
print("Your dog's name is " + you_dog.name.title() + ".")
print("Your dog's age is " + str(you_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
