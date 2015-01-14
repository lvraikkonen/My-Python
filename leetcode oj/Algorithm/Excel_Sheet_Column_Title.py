## Excel Sheet Column Title
"""
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""

def convert2title(num):
    title = ''
    while num > 0:
        num -= 1
        mod = num % 26
        title += chr(ord('A') + mod)
    return title[::-1]
