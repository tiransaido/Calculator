def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide two numbers."""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    """Simple calculator program."""
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        result = "Invalid choice. Please select a valid operation."

    # Display the result
    print("Result:", result)

if __name__ == "__main__":
    calculator()
