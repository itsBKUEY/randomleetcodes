# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#input : root 

#output: 2d array


#Plan

#create 2d array



#helper (main 2d array, index, node )

# array[index]  append node val  to array

# helper (main 2d array, index+1, node.left )
# helper (main 2d array, index+1, node.right )
#
# return main2d array 


# return 2d

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Res = []

        def levelOrderhelper(node, array, index):

            if(node is None):
                return array
                
            if(index >= len(array)):
                array.append([])

            array[index].append(node.val)

            levelOrderhelper(node.left, array, index+1)
            levelOrderhelper(node.right, array, index+1)
            return array

        return levelOrderhelper(root, Res, 0)





        


        