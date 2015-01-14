## Length of Last Word
def lengthOfLastWord(s):
    s = s.strip()
    lst = s.split(' ')
    if len(lst) == 0:
        return 0
    return len(lst.pop())
