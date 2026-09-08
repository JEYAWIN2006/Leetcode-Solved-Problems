class Solution:
    def digitCount(self, num: str) -> bool:
        count=0
        ans=[]
        n=len(num)
        for i in range(n):
            for j in range(n):
                if str(i)==num[j]:
                    count+=1
            ans.append(count)
            count=0
        return "".join(map(str,ans))==num