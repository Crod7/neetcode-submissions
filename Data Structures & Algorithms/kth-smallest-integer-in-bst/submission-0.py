# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.curr = k
        self.res = None
        self.stack = []

        def compare(root):

            if not root:
                return

            compare(root.left)

            self.stack.append(root.val)

            compare(root.right)
        compare(root)


        while k > 1:
            k -= 1
            self.stack.pop(0)
        return self.stack[0]