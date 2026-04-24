class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L=R=k=0
        for i in moves:
            if i=='L':
                L+=1
            elif i=='R':
                R+=1
            else:
                k+=1  
            g=abs(L-R)+k
        return g