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
        first_word = lines[index]
        second_word = lines[index + 1]
        third_word = lines[index + 2]
        # take set of each variable and find the union
        # remove "\n". Pop the element from the list to string
        union_with_newlines = set(first_word) & set(second_word) & set(third_word)
        union = set(union_with_newlines) - {"\n"}
        repeating_letters = union.pop()

        #convert letter in repeating_letters to its prbset value, and total them
        get_value = ascii_lookup(repeating_letters)
        total += get_value
        index += 3


print(total)
