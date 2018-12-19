inputArr = []
field = []
vsota = 0
sizeOfField = 1000

field = [[0 for x in range(sizeOfField)] for y in range(sizeOfField)] 

#for neki in field:
#    print(neki)

with open("input.txt") as inputFile:
    for line in inputFile:
        inputArr.append(line.strip())

for element in inputArr:
    tempArr = element.split(" ")
    #print(tempArr)
    X = int(tempArr[2].split(",")[0])
    Y = int(tempArr[2].split(",")[1][0:-1])
    width = int(tempArr[3].split("x")[0])
    height = int(tempArr[3].split("x")[1])
    index = tempArr[0]


    for x in range(width):
        for y in range(height):
            #print(X+x,Y+y)
            if field[X+x][Y+y] == 1:
                vsota +=1
                field[X+x][Y+y] += 1
            elif field[X+x][Y+y] == 0:
                field[X+x][Y+y] += 1
            elif field[X+x][Y+y] > 1:
                field[X+x][Y+y] += 1
print(vsota)

for element in inputArr:
    tempArr = element.split(" ")
    X = int(tempArr[2].split(",")[0])
    Y = int(tempArr[2].split(",")[1][0:-1])
    width = int(tempArr[3].split("x")[0])
    height = int(tempArr[3].split("x")[1])
    index = tempArr[0]


    doesOverlap = False

    for x in range(width):
        for y in range(height):
            if field[X+x][Y+y] > 1:
                doesOverlap = True


    if not doesOverlap:
       print(index)
