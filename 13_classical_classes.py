#Task 1
class person:
    

 def __init__(self,name,age):
   self.name = name
   self.age = age
 def hi(self):
   print("Hi my name is " +  self.name + " " + str(self.age))

Jahni = person("Jahni",16)
Jahni.hi()

#Task 2

class Animal:
  def speak(self):
    pass
class Dog(Animal):
  def speak(self):
    print("woof!")
my_dog = Dog()
my_dog.speak()

class Cat(Animal):
  def speak(self):
    print("meow!")
my_cat = Cat()
my_cat.speak()
#Task 3
class BankAccount:
  
