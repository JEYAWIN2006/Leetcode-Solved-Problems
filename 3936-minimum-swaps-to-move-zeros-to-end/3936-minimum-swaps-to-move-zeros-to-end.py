class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                count+=1
                
        for i in range(n-count,n):
            if nums[i]==0:
                count-=1
        return count               


        