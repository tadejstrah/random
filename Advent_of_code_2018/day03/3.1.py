inputArr = []

field = [[]]

with open("input.txt") as inputFile:
    for line in inputFile:
        inputArr.append(line.strip())

for element in inputArr:
    #dvomestne cifre!! popravi
    upLeftX = element[5]
    upLeftY = element[7]
    height = element[10]
    width = element[12]

    for i in range(upLeftX):
        pass
    