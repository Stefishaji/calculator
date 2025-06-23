# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def main():
    print("Welcome to the CLI Calculator!")
    print("Available operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator.")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

        # Ask if the user wants to continue
        cont = input("Do you want to perform another calculation? (yes/no): ").lower()
        if cont != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
