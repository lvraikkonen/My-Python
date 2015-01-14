## sqrt
## Implement int sqrt(int x).
def sqrt(x):
    low, high = 0, x/2 + 1
    while low <= high:
        mid = (low + high) / 2
        if mid**2 == x:
            return mid
        elif mid**2 < x:
            low = mid + 1
        else:
            high = mid - 1
    return int(high)
