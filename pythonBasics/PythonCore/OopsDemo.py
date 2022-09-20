#classes are user defined blueprint or peototype
#class has methods, class variables, instance variables, constructor

class Calculator:
    num = 100 #class variable
    #default constructor

    def __init__(self,a,b):
        self.firstNumber=a  #instance variable
        self.secondNumber=b #instance variable
        print("power")
        print(pow(self.firstNumber,2))
        print("Iam called automatically when obj is created")

    def getData(self):
        print("Iam executing a method")

    def Summation(self):
        return self.firstNumber+self.secondNumber + self.num  #to call class variable we can use self(universal), class name or object name


obj=Calculator(2, 3)  #syntax to create object
obj1=Calculator(4, 5)
obj.getData()
print(obj.Summation())
print(obj1.Summation())