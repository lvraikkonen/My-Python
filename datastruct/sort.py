## Bubble Sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            if lst[i] > lst[j]: # move larger backward
                lst[i], lst[j] = lst[j], lst[i]

    return lst

## Select Sort
def select_sort(lst):
    for i in range(len(lst)):
        minindex = i
        for j in range(i, len(lst)):
            if lst[minindex] > lst[j]:
                minindex = j
        lst[i], lst[minindex] = lst[minindex], lst[i]

    return lst

## Insert Sort
def insert_sort(lst):
    for i in range(1, len(lst)): # first element as sorted
        tmp = lst[i] # extract a item
        j = i - 1
        while j >= 0 and tmp < lst[j]:
            lst[j+1] = lst[j] # move back
            j -= 1
        lst[j+1] = tmp

    return lst

## Shell Sort : Improve for insert sort
def shell_sort(lst):
    gap = 3
    while gap > 0:
        for i in range(1, len(lst)):
            tmp = lst[i]
            j = i - gap
            while j >= 0 and tmp < lst[j]:
                lst[j+gap] = lst[j]
                j -= gap
            lst[j+gap] = tmp
        gap /= 2

    return lst

## Merge Sort
def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) / 2
    left = mergeSort(lst[:num])
    right = mergeSort(lst[num:])

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0)) # O(n)
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result += left
    else:
        result += right
    return result

## improved
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) / 2
    # recusive
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    # extra space
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result


## Quick Sort
def partition(lst, first, last):
    pivot = lst[first]
    left = first + 1
    right = last
    done = False
    while left <= right and not done:
        while left <= right and lst[left] < pivot:
            left += 1
        while left <= right and lst[right] > pivot:
            right -= 1
        if left > right:
            done = True
        else:
            # swap
            lst[left], lst[right] = lst[right], lst[left]
    # swap the pivot
    lst[first], lst[right] = lst[right], lst[first]
    return right

def quick_sort(lst, first, last):
    if first < last:
        split_point = partition(lst, first, last)

        # quick sort left
        quick_sort(lst, first, split_point-1)
        # quick sort right
        quick_sort(lst, split_point+1, last)

## test case for quick sort
l = [4, 6, 5, 3, 8, 7, 1, 2, 0, 9]
quick_sort(l, 0, len(l)-1)
## 0 1 2 3 4 5 6 7 8 9
