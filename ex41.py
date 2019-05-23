## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(Object):
    def woof():
        pr
## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a variable named name
        self.name = name

## Class Cat is-a Animal

class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Class Person is-a object

class Person(Object):
    def __init__(self, name):
        ## Person has-a name:
        self.name = name
        ## Person has-a Cat of some kind
        self.pet = None

## Employee is-a Person:

class Employee(Person):
    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Class Salmon is-a Fish
class Salmon(Fish):
    pass

## Class Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a dog:
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person

mary = Person("Mary")

## Mary has-a pet that is-a cat called Satan

mary.pet = satan

## Frank is-a Employee that has-a name and has-a salary

frank = Employee("Frank", 120000)

## Frank has-a pet named rover

frank.pet = rover

## Flipper is-a fish

flipper = Fish()

## crouse is-a Salmon

crouse = Salmon()

## harry is-a Halibut()

harry = Halibut()
