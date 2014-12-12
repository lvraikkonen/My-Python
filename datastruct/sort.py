## Bubble Sort
def bubbleSort(list):
    n = len(list)
    for i in range(0,n):
        for j in range(i,n):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    return list

## Select Sort
def selectSort(list):
    n = len(list)
    for i in range(0,n):
        minindex = i
        for j in range(i,n):
            if list[minindex] > list[j]:
                minindex = j
        list[i],list[minindex] = list[minindex],list[i]

    return list

## Insert Sort
def insertSort(list):
    for i in range(1,len(list)): # first item as sorted
        tmp = list[i] # extract a item
        j = i - 1 # sorted index
        while j >= 0 and tmp < list[j]:
            list[j + 1] = list[j] # move back
            j -= 1
        list[j + 1] = tmp ## insert value
    return list

## Merge Sort
def mergeSort(list):
    if len(list) <= 1:
        return list
    num = len(list) / 2
    left = mergeSort(list[:num])
    right = mergeSort(list[num:])

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result += left
    else:
        result += right
    return result

def merge(left,right):
    ## left and right are sorted lists
    l,r = 0,0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    ## rest data
    result += left[l:]
    result += right[r:]

    return result
