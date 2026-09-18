class Solution(object):
    def transformArray(self, nums):
        small=[]
        big=[]
        for i in nums:
            if i%2==0:
                i=0
                small.append(i)
            else:
                i=1
                big.append(i)
        return small+big
        