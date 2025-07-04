check_even_number = lambda num: num % 2 == 0
check_odd_number = lambda num: num % 2 != 0


while True:
    user_input = input("Enter a number: ")

    try:
        if user_input.isdigit():
            if check_even_number(int(user_input)):
                print(f"{user_input} is an even number.")
            elif check_odd_number(int(user_input)):
                print(f"{user_input} is an odd number.")
            else:
                print(f"{user_input} is neither even nor odd.")
        elif user_input.lower() in ['exit', 'quit', 'q']:
            print("Exiting the program.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit' to quit.")
        
