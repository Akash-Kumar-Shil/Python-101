import winsound
from datetime import datetime
from time import sleep

def play_alarm_sound():
    for x in range(10):
        winsound.Beep(1000, 800)  # Beep for 0.8 seconds

def alarm_clock(alarm_time):
    print(f"⏰ Alarm set for {alarm_time}")
    
    while True:
        now = datetime.now().strftime("%I:%M %p")
        if now == alarm_time:
            print("\n🔔 Wake up! It's time!")
            play_alarm_sound()
            break
        sleep(1)


# Example usage
# Format: HH:MM AM/PM — e.g., "07:30 AM"
user_input = input("Enter alarm time (HH:MM AM/PM): ").strip()

try:
    # Validate time format
    datetime.strptime(user_input, "%I:%M %p")
    alarm_clock(user_input)
except ValueError:
    print("❌ Invalid time format. Please use HH:MM AM/PM (e.g., 07:30 AM).")




