## Compare Version Number
"""
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
0.1 < 1.1 < 1.2 < 13.37

"""
def compare_version(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    max_len = max(len(v1), len(v2))
    for i in range(max_len):
        v1Token, v2Token = 0, 0
        if i < len(v1):
            v1Token = int(v1[i])
        if i < len(v2):
            v2Token = int(v2[i])
        # compare
        if v1Token > v2Token:
            return 1
        if v1Token < v2Token:
            return -1
    return 0
