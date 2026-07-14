# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def getHeight(root):
            if not root:
                return 0

            Left = getHeight(root.left)
            Right = getHeight(root.right)

            if abs(Left - Right) > 1:
                self.res = False

            return 1 + max(Left, Right)
            
        getHeight(root)
        
        return self.res


            

