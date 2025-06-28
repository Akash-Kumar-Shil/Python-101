def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    while True:
        choice = input("Enter choice (1/2 or 'q' to quit): ")

        if choice in ["exit", "quit", "q"]:
            # Exit the program
            print("Exiting converter. Stay warm (or cool)!")
            break

        if choice in ["1", "c to f", "celsius to fahrenheit"]:
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = celsius_to_fahrenheit(c)
                print(f"{c}°C is {f:.2f}°F")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice in  ["2", "f to c", "fahrenheit to celsius"]:
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = fahrenheit_to_celsius(f)
                print(f"{f}°F is {c:.2f}°C")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
