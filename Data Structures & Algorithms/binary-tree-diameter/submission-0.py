# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def countLength(root):
            if not root:
                return 0

            Left, Right = countLength(root.left), countLength(root.right)
            self.res = max(self.res, Left + Right)
            return max(Left, Right) + 1
        countLength(root)
        return self.res

        