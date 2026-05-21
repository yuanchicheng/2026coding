#week10-2a.py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root == None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            return max(left, right) + 1
        
        return helper(root)

