row = 1
with open ("input.txt") as file:
    for line in file:
        split_index = (int(len(line)) // 2)
        print(f"Line: {row} Split_Index: {split_index}")
        row =+ 1