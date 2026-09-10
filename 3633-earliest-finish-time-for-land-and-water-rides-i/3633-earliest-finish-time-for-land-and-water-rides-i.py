class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # land first
        landtime = float('inf')
        for i in range(len(landStartTime)):
            landtime = min(landtime, landStartTime[i] + landDuration[i])
        landans = float('inf')
        for j in range(len(waterStartTime)):
            landans = min(landans, max(landtime, waterStartTime[j]) + waterDuration[j])
        # water first
        watertime = float('inf')
        for i in range(len(waterStartTime)):
            watertime = min(watertime, waterStartTime[i] + waterDuration[i])
        waterans = float('inf')
        for j in range(len(landStartTime)):
            waterans = min(waterans, max(watertime, landStartTime[j]) + landDuration[j])
        return min(landans, waterans)
        