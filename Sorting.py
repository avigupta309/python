#Sorting

#1. Selection Sort

def Sorting(array):
    num=len(array)
    for i in range(num):
        minIndex=i
        for j in range(i+1,num):
            if array[minIndex]>array[j]:
                minIndex=j
        array[i],array[minIndex]=array[minIndex],array[i]
    print(array)

array=[1,7,9,2,5,3,4,8,6]

Sorting(array)


#2. Bubble Sort

def BubbleSorting(array):
    num=len(array)
    isSwapped=False
    for i in range(num):
        for j in range(0,num-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                isSwapped=True
        if not isSwapped:
            break
    print(array)

array=[1,7,9,2,5,3,4]
BubbleSorting(array)


def insertionSort(array):
    num=len(array)
    for i in range(1,num):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    print(array)
array=[11,5,7,1,4,9]
insertionSort(array)