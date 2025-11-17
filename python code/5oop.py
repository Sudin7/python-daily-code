#Create a class Car that takes brand, model, and year. Add a method to display its info.
class Car():
    def __init__(self,brand="",model="",year=0):
      self.brand=brand
      self.model=model
      self.year=year
    
    def getdata(self):
        self.brand=input("What is brand of the car: ")
        self.model=input("which model: ")
        self.year=int(input("which year: "))
    
    def showdata(self):
        print(f"Brand of car is {self.brand}")
        print(f"model of car is {self.model}")
        print(f"Year of car is {self.year}")
        
c1=Car()
c2=Car()

c1.getdata()
c2.getdata()

c1.showdata()
c2.showdata()
