class Knowledge_Check:
    number1 = 100

    def __int__(self, num1, num2):
        self.firstNumber = num1
        self.secondNumber = num2

    def Minus(self):
        return self.number1 - self.firstNumber - self.secondNumber

obj = Knowledge_Check()
obj.__int__(10, 20)
print(obj.Minus())
