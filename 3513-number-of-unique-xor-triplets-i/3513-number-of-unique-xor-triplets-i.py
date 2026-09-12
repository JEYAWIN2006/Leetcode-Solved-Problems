from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        op = 1

        while op <= n:
            op <<= 1

        return op