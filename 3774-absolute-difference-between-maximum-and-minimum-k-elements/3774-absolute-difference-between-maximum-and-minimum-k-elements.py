class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mins=sum(nums[:k])
        maxs=sum(nums[-k:])
        return abs(maxs-mins)