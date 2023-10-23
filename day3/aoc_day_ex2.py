index = 0
total = 0
repeating_letters = []


def ascii_lookup(letter):
    if letter.islower():
        return (ord(letter) - 96)
    else:
        return (ord(letter) - 38)

with open ("input.txt") as file:
    lines = file.readlines()
    
    # get list length, - 2, get 3 words each iteration, cannot index past
    # end of list
    while index <= len(lines) - 2:
        duplicate = []
        first_word = lines[index]
        second_word = lines[index + 1] 
        third_word = lines[index + 2]
        print(f"1: {first_word} 2: {second_word} 3: {third_word}")
        
        # compare letters in 1st and 2nd word, exclude \n matches
        # ver2 add recursion
        for i in first_word:
            for j in second_word :
                if i == j and j != "\n":
                    
                    # if j eqs k AND j isn't already in the duplicate list 
                    for k in third_word:
                        if j == k and duplicate.count(j) == 0:                
                            duplicate.append(j)
                            repeating_letters.append(j)
                           #print(f"Index: {index} Duplicate = {duplicate}")
        index += 3

# take duplicates, get ascii values and convert to prbset value     
for repeat in repeating_letters:        
    get_value = ascii_lookup(repeat)
    print(get_value)
    total += get_value

print(total)
