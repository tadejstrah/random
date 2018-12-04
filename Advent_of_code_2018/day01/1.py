sum = 0

with open("text.txt") as input:
    for line in input:
        sum += int(line)
        print(sum)


print(sum)