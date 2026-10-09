class Solution:
    def minInsertions(self, s: str) -> int:
        stack_left = []
        stack_right = []

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stack_left.append(i)
            else:
                stack_right.append(i)

            if len(stack_right) > 1 and len(stack_left) > 0 and stack_left[-1] < stack_right[-2] and stack_right[-2] + 1 == stack_right[-1]:
                stack_left.pop()
                stack_right.pop()
                stack_right.pop()

        ans = 0

        while stack_left or stack_right:
            if len(stack_right) == 0:
                ans += len(stack_left) * 2
                break
            elif len(stack_left) == 0:
                while len(stack_right) > 1:
                    if stack_right[-1] - 1 == stack_right[-2]:
                        ans += 1
                        stack_right.pop()
                        stack_right.pop()
                    else:
                        ans += 2
                        stack_right.pop()
                if len(stack_right) > 0:
                    ans += 2
                    break
            else:
                if stack_left[-1] < stack_right[-1]:
                    ans += 1
                    stack_left.pop()
                    stack_right.pop()
                else:
                    stack_left.pop()
                    ans += 2

        return ans