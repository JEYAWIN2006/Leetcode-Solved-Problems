class Solution:
    def uniformArray(self, a: list[int]) -> bool:
        return min(a)&1==1 or all(v&1==0 for v in a)