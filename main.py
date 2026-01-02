from datetime import datetime, timedelta

current_time = datetime.now()
print("Current time:", current_time.strftime("%H:%M"))

def sleep_cycle(current_time):
    cycle_length = 90
    cycles = 1
    updated_time = current_time
    for cycle in range(1, 8):
        wake_up = (updated_time + timedelta(minutes=cycle_length)).strftime("%H:%M")
        print(f"Wake up {cycles}: {wake_up}")
        cycles += 1
        updated_time += timedelta(minutes=cycle_length)
sleep_cycle(current_time)




