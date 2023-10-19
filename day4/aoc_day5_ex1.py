counter = 0

with open("input.txt") as file:
    
    for line in file:
        (first, second) = line.split(",")
        (first_one, first_two) = first.split("-")
        (second_one, second_two) = second.split("-")
    
        if int(first_one) <= int(second_one) and int(first_two) >= int(second_two):
            counter += 1
        elif int(second_one) <= int(first_one) and int(second_two) >= int(first_two):
            counter += 1
    
print(counter)