## Search Insert Position

## binary search
def searchInsert(A, target):
    first, last = 0, len(A)-1
    found = False
    while first <= last and not found:
        mid = (first + last) / 2
        if target == A[mid]:
            return mid
        else:
            if target < A[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return first
