class Solution(object):
    def leafSimilar(self, root1, root2):
        return self.findleaf(root1) == self.findleaf(root2)
        
    def findleaf(self, root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)