class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'sub':
            return self.a - self.b
        elif operation == 'mul':
            return self.a * self.b
        elif operation == 'div':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"



print("Simple Calculator")
print("Available operations: add, sub, mul, div")

a = input("Enter first number (a): ")
b = input("Enter second number (b): ")
operation = input("Enter operation type: ")

calc = Calculator(a, b)
result = calc.operate(operation)

print(f"Result of {operation} between {a} and {b} is: {result}")
