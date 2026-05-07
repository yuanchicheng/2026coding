# week11-1.py 學習目標 Binary Tree - DFS 朱2題 Easy題
# LeetCode 872. Leaf-Similar Trees
# 我們把 binary tree 裡的 leaf 組出來，看是否都相同

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []

        def helper(root):
            if root.left == None and root.right == None:  # 葉子
                a.append(root.val)  # 把值加入 a

            if root.left:
                helper(root.left)   # 如果左邊有

            if root.right:
                helper(root.right)  # 如果右邊有

        helper(root1)

        a, b = [], a

        helper(root2)

        print('a', a)
        print('b', b)

        return a == b
