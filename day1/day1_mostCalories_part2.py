total_cal = []
calories = 0
top3_elves = 0

with open("input.txt") as file:
    for line in file:
       # print(line)
        if line.strip():
            calories += int(line)
           #print(f"Calories: {calories}")
        else:
            total_cal.append(calories)
            calories = 0
        
total_cal.sort(reverse=True)
for _ in range(0, 3):
    top3_elves += total_cal[_]
    print(top3_elves)