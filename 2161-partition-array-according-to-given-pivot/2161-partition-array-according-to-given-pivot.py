class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        p=[]
        ind=[]
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i==pivot:
                p.append(i)
            elif i>pivot:
                ind.append(i)
        return l+p+ind
        