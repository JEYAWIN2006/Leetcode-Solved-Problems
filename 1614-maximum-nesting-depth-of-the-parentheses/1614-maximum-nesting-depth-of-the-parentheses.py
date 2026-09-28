class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        depth = 0

        for c in s:
            if c == "(": 
                stack.append("(")
            elif c == ")": 
                stack.pop()
            depth = max(depth,len(stack))

        if len(stack) != 0:
            raise Exception("something went wrong with stack.")

        return depth
        