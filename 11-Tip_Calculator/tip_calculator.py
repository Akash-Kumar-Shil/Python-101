def tip_calculator(total_bill, tip, split_bill):
    total_amount = total_bill + tip
    split_amount = total_amount / split_bill
    return f"Total amount: {total_amount} \n Tip amount: {tip} \n Split amount: {split_amount}"

def clear_screen():
    print("\033c", end="")


while True:
    try:
        bill_amount = float(input("Enter the bill amount: "))
        tip_amount = float(input("Enter the tip amount: "))
        split_amount = int(input("Enter the number of people splitting the bill: "))
        print(tip_calculator(bill_amount, tip_amount, split_amount))
        print("Thank you for using the tip calculator!")
        print("----------------------------------")
        user_command = input("Do you want to continue? (yes/no): ")
        if user_command.lower() == "no" or user_command.lower() == "n":
            break
        else:
            clear_screen()
            continue

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
