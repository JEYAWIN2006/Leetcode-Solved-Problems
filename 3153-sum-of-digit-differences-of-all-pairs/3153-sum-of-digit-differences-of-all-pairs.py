class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        l = len(str(nums[0]))
        dp = [Counter() for _ in range(l)]
        ans = 0
        for i in range(len(nums)):
            for index,digit in enumerate(str(nums[i])):
                if digit in dp[index]:
                    ans -= dp[index][digit]
                ans += i
                dp[index] += Counter([digit])            
        return ans