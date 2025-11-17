#2. Create a class Rectangle with methods to calculate area and perimeter(A = l × w)(P = 2(l + w))
class Rectangle():
  def __init__(self,length=0,width=0):
      self.length=length
      self.width=width
  
  def getdata(self):
      self.length=float(input("Enter lenth of rectangle"))
      self.width=float(input("Enter width of rectangle"))
  
  def area(self):
      area=self.length*self.width
      print(f"Area is {area}")
  
  def perimeter(self):
      perimeter=2*(self.length+self.width)
      print(f"Perimeter is {perimeter}") 
      
r1=Rectangle()
r1.getdata()

r1.area()
r1.perimeter()
