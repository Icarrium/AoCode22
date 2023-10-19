row = 1
sum = 0

# read through both words, return on duplicate
def find_duplicate(words): 
    
    for word in words:
         test = word
         word 

# use ascii alphabet to covent to problems letter-to-number value           
def ascii_lookup(letter):
    if letter.islower():
        return (ord(letter) - 96)
    else:
        return (ord(letter) - 38)


with open ("input.txt") as file:
    start_index = 0
    stop_index = 3

    with open ("input.txt") as file:
        lines = file.readlines()
        for line in lines[start_index: stop_index]:
            dup = find_duplicate(line)      

print(f"Sum: {sum}")


