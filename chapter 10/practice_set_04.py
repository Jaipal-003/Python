class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"The value of {self.num} square is {self.num ** 2}")

    def SquareRoot(self):
        print(f"The value of {self.num} squareRoot is {self.num ** 0.5}")

    def cube(self):
        print(f"The value of {self.num} cube is {self.num ** 3}")

    @staticmethod
    def greet():
        print("**********Hello ther welcome to the best calculator of the world***********")

a = Calculator(5)
a.greet()
a.square()    
a.SquareRoot()
a.cube() 