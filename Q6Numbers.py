class Numbers:
    def __init__(self):
        self.Value1 = 0 
        self.Value2 = 0  
    def Accept(self):
        self.Value1 = float(input("Enter the first number (Value1): "))
        self.Value2 = float(input("Enter the second number (Value2): "))
    def Addition(self):
        return self.Value1 + self.Value2
    def Subtraction(self):
        return self.Value1 - self.Value2
    def Multiplication(self):
        return self.Value1 * self.Value2
    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Error: Division by zero is not allowed."
num1 = Numbers()
num1.Accept()
print(f"Addition of {num1.Value1} and {num1.Value2}: {num1.Addition()}")
print(f"Subtraction of {num1.Value1} and {num1.Value2}: {num1.Subtraction()}")
print(f"Multiplication of {num1.Value1} and {num1.Value2}: {num1.Multiplication()}")
print(f"Division of {num1.Value1} by {num1.Value2}: {num1.Division()}")

print()
num2 = Numbers()
num2.Accept()
print(f"Addition of {num2.Value1} and {num2.Value2}: {num2.Addition()}")
print(f"Subtraction of {num2.Value1} and {num2.Value2}: {num2.Subtraction()}")
print(f"Multiplication of {num2.Value1} and {num2.Value2}: {num2.Multiplication()}")
print(f"Division of {num2.Value1} by {num2.Value2}: {num2.Division()}")