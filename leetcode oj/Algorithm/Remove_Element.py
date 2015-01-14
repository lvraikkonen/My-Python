## Remove Element
def remove_element(A, elem):
    first, last = 0, len(A)-1
    while first <= last:
        if A[first] == elem:
            # first should be removed
            A[first], A[last] = A[last], A[first]
            last -= 1
        else:
            first += 1
    return last + 1

## another solution
def remove_element(A, elem):
    j = 0
    for i in range(len(A)):
        if A[i] != elem:
            A[j] = A[i]
            j += 1
    return j
