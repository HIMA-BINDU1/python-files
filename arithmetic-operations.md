### Question

Create a Python program using a class named Calculator with methods for addition, subtraction, multiplication, and division.

Output

Addition (10 + 5): 15
Subtraction (10 - 5): 5
Multiplication (10 * 5): 50
Division (10 / 5): 2.0
Division (10 / 0): Error: Division by zero is not allowed.

### Solution

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        try:
            return self.a//self.b
        except ZeroDivisionError:
            return "division is not calculated"

a = int(input())
b = int(input())
res = Calculator(a,b)
print(res.add())
print(res.sub())
print(res.mul())  
print(res.div())
