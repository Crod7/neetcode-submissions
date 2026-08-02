# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ''

        def preorder(root):
            if not root:
                if self.res == '':
                    self.res = 'N'
                else:
                    self.res = self.res + ',N'
                return 
            
            if self.res == '':
                self.res = str(root.val)
            else:
                self.res = self.res + ',' + str(root.val)

            preorder(root.left)
            preorder(root.right)

            return
        preorder(root)
        

        return self.res

        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        array = data.split(',')
        self.i = 0

        def dfs():
            if array[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(array[self.i]))

            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
            



        
        







