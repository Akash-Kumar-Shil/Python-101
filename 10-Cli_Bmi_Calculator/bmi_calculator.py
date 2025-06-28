def calculate_bmi(weight, height):
    # BMI = weight (kg) / height^2 (m²)
    return weight / (height ** 2)

def main():
    print("Welcome to the BMI Calculator!")

    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        if weight <= 0 or height <= 0:
            print("❌ Please enter positive values for weight and height.")
            return

        bmi = calculate_bmi(weight, height)
        print(f"\nYour BMI is: {bmi:.2f}")

        # BMI categories
        if bmi < 18.5:
            print("🟡 Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("🟢 Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("🟠 Category: Overweight")
        else:
            print("🔴 Category: Obesity")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
