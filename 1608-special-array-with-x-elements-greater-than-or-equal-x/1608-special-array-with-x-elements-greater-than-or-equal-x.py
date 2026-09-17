class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)

        for i in range(1, N+1):
            k = bisect_left(nums, i) 
            if N - k == i:
                return i
        return -1