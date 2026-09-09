class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minLandFinish = min(ls + ld for ls, ld in zip(landStartTime, landDuration))
        minWaterFinish = min(ws + wd for ws, wd in zip(waterStartTime, waterDuration))
        ans1 = min(max(minLandFinish, ws) + wd for ws, wd in zip(waterStartTime, waterDuration))
        ans2 = min(max(minWaterFinish, ls) + ld for ls, ld in zip(landStartTime, landDuration))
        return min(ans1, ans2)