class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        depth=current=0
        for c in s:
            if c=="(":
                depth+=1
            else:
                depth-=1

                if depth<0:
                    depth+=1
                    current+=1
        return depth+current
