inputArr = []
checksum = 1
tempDict2 = {}

with open("input.txt") as myInput:
    for line in myInput:
        inputArr.append(line)

for line in inputArr:
    tempArr ={}
    for x in range(len(line)):
        try:
            tempArr[line[x]] += 1
        except:
            tempArr[line[x]] = 1

    #tempChcksum = 1
   # print(tempArr.values())
    nekiset = set(tempArr.values())
    for i in nekiset:
        try:
            tempDict2[i] += 1
        except:
            tempDict2[i] = 1

first = True
for i in tempDict2.values():
    if first:
        first = False
        pass
    else:
        checksum *= i
print(checksum)

        
        