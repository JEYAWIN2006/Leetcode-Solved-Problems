class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minDis = 10000
        for i in range(0, len(nums)):
            if nums[i] == target:
                if minDis > abs(i - start):
                    minDis = abs(i - start)
        return minDis


        