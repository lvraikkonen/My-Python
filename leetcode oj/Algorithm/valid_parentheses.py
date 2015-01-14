## Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
## determine if the input string is valid.

def isValid(s):
    push_set = ['(','{','[']
    pop_set = [')','}',']']
    pair = dict(zip(push_set,pop_set))
    stack = []
    for element in s:
        if element in push_set:
            stack.append(pair[element])
        elif element in pop_set:
            if not stack or element != stack.pop():
                return False
    if stack:
        return False
    else:
        return True
