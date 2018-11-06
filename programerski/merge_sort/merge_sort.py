#import random

arraycek = [4,2,67,3,5,3,43,3,2,634,53,534,534,534,5,3453,45,3523,46,23654,2645,36,4565,43,643,34,523,5436,4320,0,-2,-3]

#for x in range(10000000):
#    arraycek.append(random.randint(0,10000000))
#print("zacel")

def split(arr):
    levi = arr[:(len(arr)//2)]
    desni = arr[(len(arr)//2):]
    if len(arr) == 1:
        return arr
    levi2 = split(levi)
    desni2 = split(desni)
    l = 0
    d = 0
    arej = []
    for i in range(len(levi2)+len(desni2)):
        if l == len(levi2):
            arej.append(desni2[d])
            d += 1
        elif d == len(desni2):
            arej.append(levi2[l])
            l += 1
        elif levi2[l] < desni2[d]:
            arej.append(levi2[l])
            l += 1
        else:
            arej.append(desni2[d])
            d += 1
    return arej
print(arraycek)
print(split(arraycek))
#print("koncal")