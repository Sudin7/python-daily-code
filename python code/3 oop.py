#Create a base class Animal and derived classes Dog and Cat. Override a method sound().
class Animal():
    def sound(self):
        print("Animals make sound")

class dog(Animal):
    def sound(self):
        print("Dog barks")

class cat(Animal):
    def sound(self):
        print("Cat meows")
        
a=Animal()
a.sound()
d=dog()
d.sound()

c=cat()
c.sound()
