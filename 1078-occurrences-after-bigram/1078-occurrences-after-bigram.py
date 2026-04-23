class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        w=text.split()
        res=[]
        for i in range(len(w)-2):
             if w[i]==first and w[i+1]==second:
                   res.append(w[i+2])   
        return res