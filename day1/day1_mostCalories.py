# create list
total_cal = []
calories = 0


with open("input.txt") as file:
    for line in file:
        # tests to see if line is blank
        if line.strip():
            calories += int(line)
            
        # push elfs total calories to list, reset calories to 0
        else:
            total_cal.append(calories)
            calories = 0

# sort list in reverse order, find the highest value in 0 element        
total_cal.sort(reverse=True)
first_element = total_cal[0]
print(first_element)

