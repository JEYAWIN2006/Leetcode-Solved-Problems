class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        j = len(nums) - 1
        i = 0
        count = 0
        while i <= j:
            if i == j:
                count += int(nums[i])
            else:
                count += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        return count
