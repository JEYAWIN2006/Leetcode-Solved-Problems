class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def nondecrease(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nondecrease(nums[:i + 1] + nums[i + 2:] ) or nondecrease(nums[: i] + nums[i + 1:] )

        return True