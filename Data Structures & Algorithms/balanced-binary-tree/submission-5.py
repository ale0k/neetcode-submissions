# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        self.isBalanced(root.left)
        self.isBalanced(root.right)
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            self.balanced = False
        return self.balanced

    def height(self, root):
        if root is None:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))