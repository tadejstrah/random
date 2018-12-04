
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         if item != "":
             self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
import sys

def returnAbsolutePath(stack):
    if len(stack.items) == 0:
        sys.stdout.write("/\n")
    else:
        for item1 in stack.items:
            sys.stdout.write("/"+item1)
        sys.stdout.write("/\n")


stack1 = Stack()
contents = []
numOfLines = int(input())
inputReadCOunter = 0

while inputReadCOunter < numOfLines:
    try:
        line = input()
        inputReadCOunter += 1
    except EOFError:
        break
    contents.append(line)



#print(stack1.items)

for element in contents:
    element = element.split(" ")
    if element[0] == "pwd":
        returnAbsolutePath(stack1)
    if element[0] == "cd":
        if element[1][0] == "/":
            stack1 = Stack()
            for el in element[1].split("/"):
                if el == "..":
                    stack1.pop()
                else:
                    stack1.push(el)
        elif element[0] == "..":
            stack1.pop()
        else:
            for el in element[1].split("/"):
                if el == "..":
                    stack1.pop()
                else:
                    stack1.push(el)




    
