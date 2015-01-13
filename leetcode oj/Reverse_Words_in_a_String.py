## Reverse Words in a String
"""
For example,
Given s = "the sky is blue",
return "blue is sky the".
"""
# cheat method
def reverseWords(s):
    l = s.strip().split()
    l.reverse()
    return ' '.join(l)
