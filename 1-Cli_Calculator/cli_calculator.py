def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract x from y and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """Divide x by y and return the result."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

def main():
    print("Welcome to the CLI Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4 or 'q' to quit): ")

        if choice in ["exit", "quit", "q"]:
            # Close the calculator app
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', "add", "subtract", "multiply", "divide"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if choice in ['1', 'add']:
                print("Result:", add(num1, num2))
            elif choice in ['2', 'subtract']:
                print("Result:", subtract(num1, num2))
            elif choice in ['3', 'multiply']:
                print("Result:", multiply(num1, num2))
            elif choice in ['4', 'divide']:
                print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please choose from 1 to 4 or 'q' to quit.")

if __name__ == "__main__":
    main()
