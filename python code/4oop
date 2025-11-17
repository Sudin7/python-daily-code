# 5. Create a class Laptop with price and brand. Add a method to apply discount.
class Laptop():
    def __init__(self,price=0,brand="",discount=0):
        self.price=price
        self.brand=brand
        self.discount=discount
    
    def getdata(self): 
        self.price=float(input("The price of laptop is:"))
        self.brand=input("The brand of laptop is ")
        self.discount=float(input("how much % discount"))
        
    def discounted(self):
        Discounted=self.price-((self.discount/100)*self.price)
        print(f"The price before discount is {self.price}")
        print(f"The price after discount is {Discounted}")
        print(f"THe brand is {self.brand}")
        
l1=Laptop()
l1.getdata()
l1.discounted()
