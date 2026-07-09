# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightDiff(root: Optional[TreeNode]):
            if not root:
                return [True, 0]

            left = heightDiff(root.left)
            right = heightDiff(root.right)
            
            if left[0] is False:
                return [False, 0]
            if right[0] is False:
                return [False, 0]

            if abs(left[1] - right[1]) > 1:
                return [False, max(left[1], right[1])] 
            
            return [True, 1 + max(left[1], right[1])] 

        res = heightDiff(root)

        return res[0]




