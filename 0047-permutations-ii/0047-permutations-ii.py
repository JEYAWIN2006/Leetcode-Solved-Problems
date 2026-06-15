from itertools import permutations 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        all=list(permutations(nums)) 
        alls = set(all)  
        ans=list(alls)
        return ans