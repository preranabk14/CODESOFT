# Simple Calculator by PRERANA B K
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Select operation: +, -, *, /")
        operation = input("Enter operation: ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero.")
                return
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    calculator()
