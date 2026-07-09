# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def traver(node, list1):
           
            if(node and node.left):
                traver(node.left,list1)
            if(node):
                list1.append(node.val)
            if(node and node.right):
                traver(node.right, list1)   
            
    
        
        node = root
        listy = []

        traver(node,listy)

        return listy


            