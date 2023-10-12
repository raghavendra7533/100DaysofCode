with open("file1.txt") as f:
    lines1 = f.readlines()
lines1 = [line.strip() for line in lines1]
lines1 = [int(line) for line in lines1]

with open("file2.txt") as f:
    lines2 = f.readlines()
lines2 = [line.strip() for line in lines2]
lines2 = [int(line) for line in lines2]

result = [num for num in lines1 if num in lines2]


# Write your code above 👆
print(result)