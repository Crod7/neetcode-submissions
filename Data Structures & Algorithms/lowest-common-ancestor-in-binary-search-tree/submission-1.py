# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        first = None
        second = None

        if p.val < q.val:
            first = p
            second = q
        else:
            first = q
            second = p

        while curr:
            if first.val > curr.val:
                curr = curr.right
            elif second.val < curr.val:
                curr = curr.left
            else:
                return curr