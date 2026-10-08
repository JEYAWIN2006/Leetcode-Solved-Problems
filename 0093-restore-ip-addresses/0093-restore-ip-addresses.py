class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def BT(i,cur):
            nonlocal res
            if i==len(s):
                if len(cur)==4:
                    res.append('.'.join([str(x) for x in cur]))
                return
            if len(cur)>4:
                return
            
            BT(i+1, cur+[int(s[i])])
            if cur and cur[-1]!=0 and cur[-1]*10+int(s[i])<=255:
                cur[-1] = cur[-1]*10+int(s[i])
                BT(i+1, cur)
                cur[-1] = cur[-1]//10
        BT(0, [])
        return res