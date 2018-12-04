sum1 = 0
inputArr = []
arr = []
shoultBreak = False

with open("text.txt") as input1:
    for line in input1:
        inputArr.append(int(line))
    while True:
        for x in inputArr:
            sum1 += x
            if (sum1 in arr):
                print(sum1)
                shoultBreak = True
                break
            else:
                arr.append(sum1)
        if shoultBreak:
            break