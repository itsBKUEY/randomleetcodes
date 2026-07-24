class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        array = []

        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        while( left < right and top < bottom):
            for i in range(left,right):
                print("y", top, "x",i)
                array.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                print("y", i, "x",right-1)
                array.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1,left-1, -1):
                print("y", bottom-1, "x",i)
                array.append(matrix[bottom-1][i])
            bottom -= 1

            
            for i in range(bottom - 1,top - 1, -1):
                print("y", i, "x",left)
                array.append(matrix[i][left])
            left += 1
        
        return array

      
