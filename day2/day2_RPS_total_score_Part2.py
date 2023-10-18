match_as_num = []
outputfile = "values.txt"
total = 0
line_num = 1

def convert_to_num(letters):
    temp = ""
    for letter in letters:
        if letter == "A" or letter == "X":
            temp = temp + "1"
        elif letter == "B" or letter == "Y":
            temp = temp + "2"
        elif letter == "C" or letter == "Z":
            temp = temp + "3"
    output.write(temp + "\n")
 
def get_total_score(round):
    #print(f"Round 1: {round[1]}")

    if round[1] == "1":
        if round[0] == "1":
            return 3
        elif round[0] == "2":
            return 1
        else:
            return 2
    elif round[1] == "2":
        if round[0] == "1":
            return 4
        elif round[0] == "2":
            return 5
        else:
            return 6
    elif round[1] == "3":
        if round[0] == "1":
            return 8
        elif round[0] == "2":
            return 9
        else:
            return 7

        
with open(outputfile, "w") as output:
    with open("input.txt") as file:
        for line in file:
            convert_to_num(line)
output.close()

with open(outputfile) as results_in_num:
    for game in results_in_num:
        score = get_total_score(game)
        total += score
        print(f"Line number {line_num}: {score}  Total Score: {total}")
        line_num += 1
        
print(total)

    

    

    

        