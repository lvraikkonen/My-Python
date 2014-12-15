class Solution:
    # @return a boolean
    def isValid(self, s):
        push_set = ("(","[","{")
        pop_set = (")","]","}")
        pair = dict(zip(push_set,pop_set))

        stack = []
        for element in s:
            if element in push_set:
                stack.append(pair[element])
            elif element in pop_set:
                if not stack or element != stack.pop():
                    return False
        if not stack:
            return True
        else:
            return False


s = "({[asc]asc}"
sol = Solution()
sol.isValid(s)