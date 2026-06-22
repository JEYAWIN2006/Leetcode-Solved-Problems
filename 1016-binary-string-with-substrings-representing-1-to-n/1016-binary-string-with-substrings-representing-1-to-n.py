class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for x in range(1,n+1):
            temp=bin(x)[2:]
            print(temp)
            if temp not in s:
                return False
        return True