## Valid Palindrome

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

"""
def isPalindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        # only char and digit left
        while i < j and not (s[i].isdigit() or s[i].isalpha()):
            i += 1
        while i < j and not (s[j].isdigit() or s[j].isalpha()):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i+1, j-1
    return True
