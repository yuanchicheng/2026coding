#week10-6.py
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def helper(root):
            if root == None:
                return 0, 0   # 左邊最長、右邊最長
            
            Lans1, Lans2 = helper(root.left)
            Rans1, Rans2 = helper(root.right)
            
            self.ans = max(self.ans, Lans2 + 1, Rans1 + 1)
            
            return Lans2 + 1, Rans1 + 1
        
        helper(root)
        return self.ans - 1

