total_cal = []
calories = 0

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
first_element = total_cal[0]
print(first_element)