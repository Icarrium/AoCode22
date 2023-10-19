total_cal = []
calories = 0
top3_elves = 0


with open("input.txt") as file:
    for line in file:
        # tests to see if line is blank
        if line.strip():
            calories += int(line)
           #print(f"Calories: {calories}")
           
        # push elfs total calories to list, reset calories to 0
        else:
            total_cal.append(calories)
            calories = 0
        
# sort list in reverse order, find highest 3 elements, sum values
total_cal.sort(reverse=True)
for _ in range(0, 3):
    top3_elves += total_cal[_]
    print(top3_elves)
    
    