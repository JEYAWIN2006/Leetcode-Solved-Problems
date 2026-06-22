class Solution:
    def minimumDeletions(self, s: str) -> int:
        b=0
        d=0
        for char in s:
            if char=='a':
                d=min(d+1,b)
            else:
                b+=1   
        return d
