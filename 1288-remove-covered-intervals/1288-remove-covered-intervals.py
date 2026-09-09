class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        res = temp = 0
        for _, j in intervals:
            if j > temp:
                res += 1
            temp = max(temp, j)        
        return res
