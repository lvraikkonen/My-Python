## Reverse Integer

"""
Consider 2 cases:
- reverse overflow
- positive/negative
"""
def reverse(x):
    if x == 0:
        return 0
    negative = False
    if x < 0:
        negative = True
        x = -x
    rev = 0
    while x != 0:
        rev = rev * 10 + x % 10
        x /= 10
    if rev < 2147483647:
        if not negative:
            return rev
        else:
            return -rev
    else:
        return 0
