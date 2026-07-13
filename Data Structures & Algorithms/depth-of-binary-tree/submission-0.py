# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        def delve(node, count):
            if(not node):
                return count
            return max(delve(node.left, count+1), delve(node.right, count+1))

        count = 0

        return delve(root,count)

