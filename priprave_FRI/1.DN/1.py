raw_data = input().split(" ")
data = []
for i in raw_data:
    data.append(int(i))
import sys

oneSolutionAlreadyPrinted = False

if data[0]==0 and data[1] == 0:
    if not oneSolutionAlreadyPrinted:
        sys.stdout.write(str(5))
        oneSolutionAlreadyPrinted = True
elif data[0] == 0:
    if not oneSolutionAlreadyPrinted:
        sys.stdout.write("No solution")
        oneSolutionAlreadyPrinted = True

else:
    no_solution = True
    for x in range(-1001,1001):  #od -100 do 100
        #print((x-10)**data[2])
        #print(data[1]/data[0])
        #print()
        if ((data[1]/data[0])%1 == 0):
            if((x)**data[2] == int(data[1]/data[0])):
                no_solution = False
                if not oneSolutionAlreadyPrinted:
                    sys.stdout.write(str(x))
                    oneSolutionAlreadyPrinted = True

                #print(x-10)
    #print(no_solution)
    if no_solution:
        if not oneSolutionAlreadyPrinted:
            sys.stdout.write("No solution")
            oneSolutionAlreadyPrinted = True

