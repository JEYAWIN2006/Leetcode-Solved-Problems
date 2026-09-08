class Solution:
    def countCommas(self, n: int) -> int:
        m=len(str(n))
        if m<=3:
            return 0
        a=n-1000
        return a+1
        