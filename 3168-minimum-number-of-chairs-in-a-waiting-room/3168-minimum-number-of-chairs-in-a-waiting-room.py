class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        res = 0

        for i in range(len(s)):
            if chairs == 0 and s[i] == 'E':
                res += 1
            elif chairs > 0 and s[i] == 'E':
                chairs -= 1
            elif s[i] == 'L':
                chairs += 1

        return res