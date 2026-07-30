# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubtreehelper(p, q):
            if(p is None and q is None):
                return True
            if(p is None or q is None):
                return False
            if(p.val == q.val):
                return (isSubtreehelper(p.left,q.left) and isSubtreehelper(p.right,q.right))


        if(root is None or  subRoot is None):
            return False
        
        if(root.val == subRoot.val and isSubtreehelper(root,subRoot)):
            return True




        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)





        