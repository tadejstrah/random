numOfLines = int(input())
inputReadCOunter = 0
contents = []
splitted = []
dictionary = {}
def findKeyByValue(dict1,value1):
    for key, value in dict1.items():
        if value1 == value:
            return key
            
while inputReadCOunter < numOfLines:
    try:
        line = input()
        inputReadCOunter += 1
    except EOFError:
        break
    contents.append(line)
for element in contents:
    splitted.append(element.split(" "))
for element in splitted:
    if (not (element[0] in dictionary)):
        if not(element[0] in dictionary.values()):
            dictionary[element[0]] = element[1]
    if element[0] in dictionary.values(): 
        dictionary[findKeyByValue(dictionary,element[0])] = element[1]
import sys
sys.stdout.write(str(len(dictionary))+"\n")
#print(len(dictionary))
for key, value in dictionary.items():
    out = str(key)+" "+str(value) +"\n"
    sys.stdout.write(out)
    #print(key,value)
