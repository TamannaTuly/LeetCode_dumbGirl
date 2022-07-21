class Solution:
    def isValid(self, s: str) -> bool:
        openList = ['[', '{', '(']
        closeList = [']', '}', ')']
        stack = []

        for i in s:
            if i in openList:
                stack.append(i)
            else:
                pos = closeList.index(i)
                if (len(stack) > 0) and (openList[pos] == stack[len(stack) - 1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
