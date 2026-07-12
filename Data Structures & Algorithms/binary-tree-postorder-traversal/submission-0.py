# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node,array):
            if(not node):
                return
            postorder(node.left, array)
            postorder(node.right, array)
            array.append(node.val)
        
        array = []
        postorder(root,array)
        return array 