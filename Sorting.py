# #Sorting

# #1. Selection Sort

# def Sorting(array):
#     num=len(array)
#     for i in range(num):
#         minIndex=i
#         for j in range(i+1,num):
#             if array[minIndex]>array[j]:
#                 minIndex=j
#         array[i],array[minIndex]=array[minIndex],array[i]
#     print(array)

# array=[1,7,9,2,5,3,4,8,6]

# Sorting(array)


# #2. Bubble Sort

# def BubbleSorting(array):
#     num=len(array)
#     isSwapped=False
#     for i in range(num):
#         for j in range(0,num-i-1):
#             if array[j]>array[j+1]:
#                 array[j],array[j+1]=array[j+1],array[j]
#                 isSwapped=True
#         if not isSwapped:
#             break
#     print(array)

# array=[1,7,9,2,5,3,4]
# BubbleSorting(array)


# def insertionSort(array):
#     num=len(array)
#     for i in range(1,num):
#         key=array[i]
#         j=i-1
#         while j>=0 and key<array[j]:
#             array[j+1]=array[j]
#             j-=1
#         array[j+1]=key
#     print(array)
# array=[11,5,7,1,4,9]
# insertionSort(array)



#4. merge sort


def mergeArray(leftArray,rightArray):
    leftArraySize,rightArraySize=len(leftArray),len(rightArray)
    i,j=0,0
    merge_Array=[]
    while i<leftArraySize and j<rightArraySize:
        if leftArray[i]<=rightArray[j]:
            merge_Array.append(leftArray[i])
            i+=1
        else:
            merge_Array.append(rightArray[j])
            j+=1
    if i<leftArraySize:
        while i<leftArraySize:
            merge_Array.append(leftArray[i])
            i+=1
    if j<rightArraySize:
        while j<rightArraySize:
            merge_Array.append(rightArray[j])
            j+=1
    return merge_Array

def mergeSort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    leftArray=array[:mid]
    rightArray=array[mid:]
    leftArray=mergeSort(leftArray)
    rightArray=mergeSort(rightArray)
    return mergeArray(leftArray,rightArray)

array=[3,7,9,2,4,7,9]
returnAnswer=mergeSort(array)
print(returnAnswer)