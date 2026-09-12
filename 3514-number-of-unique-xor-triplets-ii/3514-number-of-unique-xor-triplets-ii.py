class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        size: int = len(nums)
        if size == 1:
            return 1
        xorSet: set[int] = set()
        setList: set[int] = set()
        for i in range(0, len(nums)):
            for j in range(i+1, size):
                xorSet.add(nums[i] ^ nums[j])

        for ele in xorSet:
            for i in range(0, size):
                setList.add(ele ^ nums[i])

        return len(setList)