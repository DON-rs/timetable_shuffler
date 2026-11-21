# Timetable for 1st Semester

import random

todos_arr = [
    "Team Project",
    "Maths Sheets",
    "Computer Engineering",
    "Computer Architecture",
    "Programming 1",
]
gym_arr = ["Chest", "Back", "Shoulders", "Arms", "Core", "Legs"]

def frequency_distrib(task_arr):

    while True:
        try:
            global daily_slots
            daily_slots = int(input("Number of tasks per day: "))
            if daily_slots < 1 or daily_slots > len(task_arr):
                print("Cannot be less than 1 or greater than range of tasks")
                continue
            else:
                break
        except ValueError:
            print(f"Input must be integer")

    total_slots = daily_slots * 7
    task_frequency = total_slots // len(task_arr) # Try to evenly spread slots
    remainder_slots = total_slots % len(task_arr) # Remaining slots for priority tasks

    task_frequency_table = {}

    for i in range(len(task_arr)):
        task_frequency_table[task_arr[i]] = task_frequency

    while remainder_slots > 0:

        for task in task_frequency_table:
            if remainder_slots > 0:
                print(task_frequency_table)
                print(f"Remaining slots: {remainder_slots}")

                while True:
                    try:
                        priority_count = int(input(f"Enter priority slots for {task}: "))
                        if priority_count < 0 or priority_count > remainder_slots:
                            print("Out of range, try again ...")
                            continue
                        elif priority_count == 0:
                            print(f"Skipping to next task ...")
                            break
                        else:
                            task_frequency_table[task] += priority_count
                            remainder_slots -= priority_count
                            break
                    except ValueError:
                        print(f"Input not an integer")
            else:
                break

    return task_frequency_table

def chunk_shuffle(original_freq):
    success = False  # Stop condition for outer retry loop

    while not success:
        frequency_table = original_freq.copy()
        chunk_list = [[] for _ in range(7)]
        day_num = 0
        success = True  # Assume success until a fail occurs

        while day_num < len(chunk_list):
            task_arr_temp = list(frequency_table.keys())

            while len(chunk_list[day_num]) < daily_slots:
                if len(task_arr_temp) == 0:
                    success = False  # Mark failure
                    break  # Break out of inner while loop

                selected_task = random.choice(task_arr_temp)

                # If no more slots from task
                if frequency_table[selected_task] == 0:
                    frequency_table.pop(selected_task)
                    task_arr_temp.remove(selected_task)

                # Avoid duplicates within same chunk
                elif selected_task in chunk_list[day_num]:
                    task_arr_temp.remove(selected_task)

                else:
                    chunk_list[day_num].append(selected_task)
                    frequency_table[selected_task] -= 1

            if not success:
                break  # Exit weekly generation and retry from scratch
            day_num += 1

    # Only printed if schedule generation succeeded
    random.shuffle(chunk_list)
    for i in range(len(chunk_list)):
        print(f"Day {i+1}: {chunk_list[i]}")

while True:
    arr_option = input(
        "--- TASK GROUP ---\n"
        "[1] TODOS\n"
        "[2] Gym\n\n"
        "Option: "
    )
    if arr_option not in ("1", "2"):
        continue
    else:
        if arr_option == "1":
            chosen_arr = todos_arr
        elif arr_option == "2":
            chosen_arr = gym_arr

        chosen_freq = frequency_distrib(chosen_arr)
        chunk_shuffle(chosen_freq)

        repeat_flag = input("Type n to exit: ")
        if repeat_flag.lower() == "n":
            break