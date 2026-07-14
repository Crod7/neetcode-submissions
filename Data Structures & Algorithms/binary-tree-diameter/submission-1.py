# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def getHeight(root):
            if not root:
                return 0

            Left = getHeight(root.left)
            Right = getHeight(root.right)
            self.res = max((Left + Right), self.res)

            return 1 + max(Left, Right)
        getHeight(root)
        return self.res
    

        