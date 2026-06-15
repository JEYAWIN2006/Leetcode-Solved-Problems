class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        k=(s+s)
        return s in k[1:-1]