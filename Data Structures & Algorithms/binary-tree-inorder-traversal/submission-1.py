# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(array, node):
            if(node and node.left):
                traverse(array, node.left)
                
            if(node):
                array.append(node.val)
            
            if(node and node.right):
                traverse(array, node.right)
            return array




        array = []
        
        node = traverse(array,root)

        return array