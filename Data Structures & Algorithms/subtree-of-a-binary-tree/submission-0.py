# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(root, subRoot):
            if not root and not subRoot:
                return True
            if root and not subRoot:
                return False
            if not root and subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return (compare(root.left, subRoot.left) and compare(root.right, subRoot.right))

        if not root: return False
        if not subRoot: return True

        if compare(root, subRoot):
            return True
        
        return ( self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot) )


