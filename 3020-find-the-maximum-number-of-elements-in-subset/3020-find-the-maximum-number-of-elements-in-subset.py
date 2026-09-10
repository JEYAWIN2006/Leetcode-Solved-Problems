from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        h = {}

        for num in nums:
            h[num] = h.get(num, 0) + 1

        ones = h.get(1, 0)

        op = ones if ones % 2 else ones - 1

        h.pop(1, None)

        for num in h:
            tmp = 0
            x = num

            while x in h and h[x] > 1:
                tmp += 2
                x *= x

            op = max(op, tmp + (1 if x in h else -1))

        return op