Didn’t like spending time making a new timetable whenever tasks need adjusting, so I created a Python script to evenly distribute then randomly allocate tasks throughout a week depending on the number of slots per day.

Example: I want to have 3 slots per day (so 21 total slots in a week for allocating tasks). The script will aim for each task to have the same total frequency. If there are any remainder slots, they become priority slots and can be allocated to any tasks that require more slots / attention.

The frequencies are set, and now the script uses Python’s random module with the objective of allocating the tasks in a non-orderly fashion. After the seven days are filled, the day “chunks” are shuffled to further minimise repetition before the final timetable is outputted.
