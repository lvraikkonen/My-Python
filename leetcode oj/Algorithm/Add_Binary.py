## Add Binary
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""
def addBinary(a, b):
    res, carry, len_a, len_b, i = "", 0, len(a), len(b), 0
    for i in range(max(len_a, len_b)):
        sum = carry
        if i < len_a:
            sum += int(a[-(i + 1)])
        if i < len_b:
            sum += int(b[-(i + 1)])
        carry = sum / 2
        sum = sum % 2
        res = "{0}{1}".format(sum, res)
    if carry == 1:
        res = "1" + res
    return res
