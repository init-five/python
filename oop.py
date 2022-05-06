# classes are user defined prototypes
# class will have methods, class variables, instance variables, constructors
class Calculator:
    num = 100

    # default constructor
    def __int__(self, a, b):
        # instance variables
        self.firstNumber = a
        self.secondNumber = b
        print("I am called when constructor is called")

    def getData(self):
        print("I am now executing this as a method in a class")

    def Sum(self):
        # you can also do self.num
        return self.firstNumber + self.secondNumber + Calculator.num


# now everything here is outside the class
# creating an object of the class
obj = Calculator()
# to call the method present in the class
obj.getData()
# to call the variable in the class
print(obj.num)
# to call the constructor
obj.__int__(2, 3)
print(obj.Sum())

# another object
obj1 = Calculator()
obj1.__int__(5, 5)
print(obj1.Sum())