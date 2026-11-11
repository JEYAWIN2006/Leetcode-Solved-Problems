class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        srt,mn = sorted([(cost1,need1),(cost2,need2)]), min(need1,need2)
        return (
            costBoth * max(need1,need2)               if costBoth <= srt[0][0] else
            costBoth * mn + 
            srt[0][0]*(srt[0][1] -mn) +
            min(srt[1][0], costBoth) *(srt[1][1] -mn) if costBoth < cost1+cost2 else
            cost1*need1 + cost2*need2
        )
        