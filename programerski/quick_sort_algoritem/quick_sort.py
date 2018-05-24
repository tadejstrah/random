import random

arr = [3,2,6,3,15,15,5,3,4,7]

#for x in range(1000000):
 #   arr.append(random.randint(0,1000000))

#print("zacel")

def sort(arraycek):
    if len(arraycek) <= 1:
        return arraycek
    pivot = arraycek[0]
    arr1 = []
    arr2 = []
    for i in range(1,len(arraycek)):
        if arraycek[i] <= pivot:
            arr1.append(arraycek[i])
        else:
            arr2.append(arraycek[i])
    arr1 = sort(arr1)
    arr2 = sort(arr2)
    return arr1 + [pivot] + arr2

#print(arr)
print(sort(arr))
#print("koncal")

def sort2(arraycek):
    if len(arraycek) <= 1:
        return arraycek
    pivot = arraycek[0]
    arr1 = []
    arr2 = []
    for i in arraycek[1:]:
        if i <= pivot:
            arr1.append(i)
        else:
            arr2.append(i)
    arr1 = sort(arr1)
    arr2 = sort(arr2)
    return arr1 + [pivot] + arr2


print(sort2(arr))