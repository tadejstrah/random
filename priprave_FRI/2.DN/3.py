numberOfNumber = int(input())
rawdata = input()
data = []
resultsArray = []

rawdata = rawdata.split(" ")
for i in rawdata:
    data.append(int(i))

from multiprocessing import Queue

queue = Queue()

for i in data:
    queue.put(i)

import copy

for index in range(len(data)):
    tempQueue = Queue()
    for i in data:
        tempQueue.put(i)
    #tempQueue = queue
   
    #print("originalqueue size ")
    #print(queue.qsize())
    
    #print(str(index)+"index1")
    if index != 0:
       # print("index")
       # print(index)
        #print()
        for i in range(index):
           # print(str(i)+"index")
            neki = tempQueue.get()
            print(neki)
            
            #print(tempQueue.qsize())
       # print("tempqueue size")
        #print(tempQueue.qsize())

    if tempQueue.qsize() >2:
        firstEl = tempQueue.get()
        #print(firstEl)
        secondEl = tempQueue.get()
        #print(secondEl)
        counterNezadovoljstva = 0
        while firstEl > secondEl:
            secondEl = tempQueue.get()
            counterNezadovoljstva += 1
            #print("counter: "+str(counterNezadovoljstva))
            print(secondEl)    
        resultsArray.append(counterNezadovoljstva-1)
    #break


print(resultsArray)

def checkSmallerneki(list,index):
    return

