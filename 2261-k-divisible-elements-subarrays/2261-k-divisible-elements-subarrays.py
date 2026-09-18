class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n=len(nums)
        ans=set()
        for i in range(n):
            for j in range(i,n):
                sub=nums[i:j+1]
                c=0
                for ch in sub:
                    if ch%p==0:
                        c+=1
                if c<=k:
                    ans.add(str(sub))
        return len(ans)