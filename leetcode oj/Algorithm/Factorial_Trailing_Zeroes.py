## Factorial Trailing Zeroes
"""
Given an integer n, return the number of trailing zeroes in n!.
"""

def trailing_zeros(n):
    result = 0
    while n >= 5:
        result += n/5
        n /= 5
    return result
