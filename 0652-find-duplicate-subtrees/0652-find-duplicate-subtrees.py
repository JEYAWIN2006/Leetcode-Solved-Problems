class Solution:
    def __init__(self):
        self.hash = defaultdict(bool)
        self.ans = []
    
    def get_ans(self, root, s):
        if root:
            lst = self.get_ans(root.left, -1) + [root.val] + self.get_ans(root.right, 1)
            tpl = tuple(lst)
            if tpl in self.hash:
                if self.hash[tpl] == True:
                    self.ans.append(root)
                    self.hash[tpl] = False
            else:
                self.hash[tpl] = True
            return lst
        return [s]
            
        

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.get_ans(root, 0)
        return self.ans