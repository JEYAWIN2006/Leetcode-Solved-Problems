class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        sub=[]
        for i in range(0,len(nums)):
            sub.append(nums[i]-i)
        print(sub)
        maps={}
        for ele in sub:
            if ele in maps:
                maps[ele]+=1
            else:
                maps[ele]=1
        ans=0
        for ele in maps:
            x=maps[ele]
            ans+=(x*(x-1))//2
        print(ans)
        total=(len(nums)*(len(nums)-1))//2
        return total-ans