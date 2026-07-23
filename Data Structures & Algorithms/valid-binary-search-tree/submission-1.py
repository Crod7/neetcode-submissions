# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.stack = []
        self.res = True

        def runCode(root):
            if not root:
                return
            
            runCode(root.left)

            if self.stack and root.val <= self.stack[-1]:
                self.res = False

            self.stack.append(root.val)

            runCode(root.right)
        
        runCode(root)

        return self.res
        