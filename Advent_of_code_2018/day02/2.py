inputArr = []


with open("input.txt") as myInput:
    for line in myInput:
        inputArr.append(line.strip())

def getDifferentChar(str1, str2):
    res = []
    res2 = []
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            res.append(str1[i])
            res.append(str2[i])
            res2.append(str1)
            res2.append(str2)
    return [res, res2]
    


for x in range(len(inputArr)):
    for y in range(x,len(inputArr)):
        if len(getDifferentChar(inputArr[x],inputArr[y])[0]) == 2:
            print(getDifferentChar(inputArr[x],inputArr[y])[1])


