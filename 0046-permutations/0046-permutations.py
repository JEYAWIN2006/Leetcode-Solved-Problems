class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def p(x):
            if len(x)==1:
                return [x]
            f= [x[0]]
            li = p(x[1:])
            ans=[]
            for i in li:
                for j in range(len(i)+1):
                    ans.append(i[:j]+f+i[j:])
            return ans
        return p(nums)
        
        