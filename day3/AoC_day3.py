row = 1
sum = 0

# read through both words, return on duplicate
def find_duplicate(first, second):
    for i in first:
        for j in second:
            if i == j:
                return j

# use ascii alphabet to covent to problems letter-to-number value           
def ascii_lookup(letter):
    if letter.islower():
        return (ord(letter) - 96)
    else:
        return (ord(letter) - 38)


with open ("input.txt") as file:
    for line in file:
        # find length of string; use floor div split into 2 eq len words
        split_index = (int(len(line)) // 2)
        first_word = line[:split_index]
        second_word = line[split_index:]
        #print (first_word + " " + second_word)
        
        dup = find_duplicate(first_word, second_word)
        get_value = ascii_lookup(dup)
        sum += get_value
        
        #print(f"{row}: {dup} index: {split_index}")
        #row += 1

print(f"Sum: {sum}")


