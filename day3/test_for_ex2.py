start_index = 0
stop_index = 3

with open ("input.txt") as file:
    lines = file.readlines()
    for line in lines[start_index: stop_index]:
        dup = find_duplicate(lines)        

