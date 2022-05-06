# importing class from other python file
from oop import Calculator


# inheriting "calculator" parent class in the child class
class Child(Calculator):
    num2 = 200

    # def __int__(self):
        # calling parent constructor
        # 2 and 10 are the values which are used as firstnumber and secondnumber
        # in the parent class sum function
        # Calculator.__int__(self, 2, 10)

    def getCompleteData(self):
        # num variable is coming from the parent class
        # Sum is also a method from parent class
        return self.num2 + self.num


obj = Child()
print(obj.getCompleteData())
