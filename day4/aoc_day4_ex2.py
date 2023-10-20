counter = 0

with open("input.txt") as file:
    
    for line in file:
        (first, second) = line.split(",")
        (first_low, first_high) = first.split("-")
        (second_low, second_high) = second.split("-")


        if int(first_low) <= int(second_high) and int(first_low) >= int(second_high):
            counter += 1
        elif int(first_high) >= int(second_low) and int(first_high) <= int(second_high):
            counter += 1
        elif int(first_low) <= int(second_low) and int(first_high) >= int(second_high): 
            counter += 1
        elif int(second_low) <= int(first_high) and int(second_low) >= int(first_high):
            counter += 1
        elif int(second_high) >= int(first_low) and int(second_high) <= int(first_high):
                counter += 1
        elif int(second_low) <= int(first_low) and int(second_high) >= int(first_high):
                counter += 1
                
print(counter)