## Excel Sheet Column Number
"""
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
"""
def title2number(s):
    result = 0
    index = 0
    for c in s[::-1]:
        # from end to start
        result += (ord(c) - ord('A') + 1) * (26**index)
        index += 1
    return result
