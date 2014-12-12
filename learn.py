def anagram1(s1,s2):
    """ identify if two strings are anagram """
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1
    return stillOK

def anagram2(s1,s2):
    alist = list(s1)
    blist = list(s2)

    alist.sort()
    blist.sort()

    matched = True
    pos = 0
    while pos<len(alist) and matched:
        if alist[pos] == blist[pos]:
            pos += 1
        else:
            matched = False
    return matched


s1 = 'hello'
s2 = 'loahe'

anagram2(s1,s2)