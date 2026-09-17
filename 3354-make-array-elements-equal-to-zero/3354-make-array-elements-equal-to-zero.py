class Solution:
    
    def countValidSelections(self, nums: List[int]) -> int:
        def movement(i , f):
            while i >= 0 and i < n:
                if (i == 0 and temp[i] == 0) or (i == n and temp[i] == 0):
                    return 
                if f == 'r':
                    if temp[i] > 0:
                        temp[i] -= 1
                        f = 'l'
                        i -= 1
                    else:
                        i += 1
                else:
                    if temp[i] > 0:
                        temp[i] -= 1
                        f = 'r'
                        i += 1
                    else:
                        i -= 1


        res = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                temp = nums[:]
                movement(i+1 , 'r')
                if sum(temp) == 0:
                    res += 1
                temp = nums[:]
                movement(i-1 , 'l')
                if sum(temp) == 0:
                    res += 1
        return res
                    

            