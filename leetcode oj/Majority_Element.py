## Majority Element
"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
"""

def majority_element(num):
    if len(num) == 0:
        return num[0]
    count = len(num) // 2
    d = dict.fromkeys(num, 0)
    for item in num:
        d[item] += 1
    result = []
    for key, val in d.items():
        result.append((val, key))
    # largest at end
    result.sort()
    if result[-1][0] >= count:
        return result[-1][1]
