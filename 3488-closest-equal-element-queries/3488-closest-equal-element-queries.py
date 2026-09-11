class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ndic,nidx,n = defaultdict(list), [], len(nums)
        for i,num in enumerate(nums): nidx.append(len(ndic[num])); ndic[num].append(i)
        return [
            -1 if (nq:= len(lq))<2 else min(
                a:= abs(lq[iq] - lq[(iq+1)%nq]),    n-a,
                b:= abs(lq[iq] - lq[(iq+nq-1)%nq]), n-b
            )
            for q      in queries
            for lq,iq  in [(ndic[nums[q]], nidx[q])]
        ]

        