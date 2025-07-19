from random import randint

def sorted(nList):
    n = len(nList)
    for i in range(0,n-1):
        if nList[i] > nList[i+1]:
            return False
    return True

def shuffle(nList):
    n = len(nList)
    for i in range(0,n):

        j = randint(0, n-1)
        nList[i], nList[j] = nList[j], nList[i]

    return nList

def bogoSort(nList):
    while not sorted(nList):
        shuffle(nList)

#Test
tmp = [1,6,9,7,8,13,3,4]
bogoSort(tmp)
print(tmp)




