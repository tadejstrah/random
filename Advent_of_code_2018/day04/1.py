inputArr = []
guards = {int:[int]}


import datetime, time




with open("input.txt") as inputFile:
    for line in inputFile:
        inputArr.append([line.strip(),0])

for neki in range(len(inputArr)):
    element = inputArr[neki]
    #print(element[0][1:5],element[0][6:8],element[0][9:11],element[0][12:14],element[0][15:17])
    myTime = datetime.datetime(int(element[0][1:5]),int(element[0][6:8]),int(element[0][9:11]),int(element[0][12:14]),int(element[0][15:17]))
   # print(time)
    ordinalTime = time.mktime(myTime.timetuple())
    inputArr[neki][1] = ordinalTime    
inputArr.sort(key=lambda x: x[1])



for element in inputArr:
    if element[0][19] == "G":

        print("neki")