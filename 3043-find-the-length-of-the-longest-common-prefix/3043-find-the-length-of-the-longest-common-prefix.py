class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans,trie = 0, dict()
        for num in arr1:
            node = trie
            for d in str(num):
                if not node.get(d):  node[d] = dict()
                node = node[d]
        for num in arr2:
            node = trie
            for i,d in enumerate(str(num), 1):
                if  node.get(d) is None: break
                ans,node = max(ans, i), node[d]
        return  ans
      