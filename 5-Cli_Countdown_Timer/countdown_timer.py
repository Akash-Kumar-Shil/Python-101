import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time left: {timer_format}", end="")
        time.sleep(1)
        seconds -= 1
    print("\r⏰ Time's up!                  ")

def main():
    try:
        total_seconds = int(input("Enter time in seconds: "))
        print("Countdown started!")
        countdown(total_seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")

if __name__ == "__main__":
    main()

