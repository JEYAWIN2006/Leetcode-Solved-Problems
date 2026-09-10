class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        s = list(s)
        l = len(s)

        s[0] = '2'
        bottom_pointer = 1

        for i in range(l):
            if s[i] == '2':
                for j in range(max(bottom_pointer, i+minJump), min(i+maxJump+1,l)):
                    if s[j] == '0':
                        s[j] = '2'
                bottom_pointer = min(i+maxJump+1,l)
        
        return s[-1] == '2'
