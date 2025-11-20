add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Error: Invalid operation"
        
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numbers.")

if __name__ == "__main__":
    calculator()
