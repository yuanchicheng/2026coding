class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        counter[0] = 1
        
        def helper(root, total):
            if root == None:
                return 0
            
            total += root.val
            
            ans = counter[total - targetSum]
            counter[total] += 1
            
            ans += helper(root.left, total)
            ans += helper(root.right, total)
            
            counter[total] -= 1
            
            return ans
        
        return helper(root, 0)

