import random

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self,newname=""):
        self.name = newname

    def set_age(self,newage):
        self.age = newage

    def __str__(self):
        return "animal: "+ str(self.name) + " : "+ str(self.age)

class Cat(Animal):
    def speak(self):
        print ("meao")

    def __str__(self):
        return "Cat :" + str(self.name) +  " : "+ str(self.age)

class Rabit(Animal):
    def speak(self):
        print("meek")

    def __str__(self):
        return "Rabbit :" + str(self.name) + " : "+ str(self.age)



class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print ("Hello")

    def age_diff(self,other):
        diff = self.get_age() - other.get_age()

        if self.age > other.age:
            print(self.name , "is ", diff , " years older than ",other.name)
        else:
            print(self.name , "is ", -diff, "years younger than ", other.name)

    def __str__(self):
        return "Person :" + str(self.name) + ":" + str(self.age)


class Student(Person):
    def __init__(self, name , age, major = None):
        Person.__init__(self,name,age)
        self.major = major

    def change_major(self,major):
        self = major

    def speak(self):
        r=random.random()

        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r <5:
            print(" I need sleep ")
        elif 0.5 <=r <0.75:
            print(" I should eat ")
        else:
            print(" I am watching TV")

    def __str__(self):
        return " Student " + str(self.name) + ": "+ str(self.age) +" : " + str(self.major)


def  mighty(mo):
    print(mo)


per = Person("Mike",15)
print(mighty(per.speak()))


#student = Student("Nambale ",45, "Chemistry ")
#print(student)

#student.change_major("Maths")
#print(student)


#eric = Person("Eric ", 56)
#john = Person("John ", 70)

#print(eric.get_age())

#print(eric.age_diff(john))

#jelly = Cat(6)
#jam = Rabit(89)
#jam.set_name("Miha")
#print(jam.speak())
#print(jam)

#b = Animal(6)
#print(b)
#b.set_age(89)
#b.set_name("Mike")
#print(b.get_age())
#print(b.get_name())
#print(b.age)

#jelly.set_name(' James')

#print(jelly)
#print(jelly.get_name())


