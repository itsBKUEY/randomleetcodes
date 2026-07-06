class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        length = len(matrix[0])
        r = (len(matrix)*length)-1

        def Matrix(numb):
            array = numb // length
            spot = numb % length 

            return matrix[array][spot]
        
        
        while(l<= r):
            m = (l+r)//2
            v = Matrix(m)

            if(v == target):
                return True
            if(v > target):
                r = m-1
            else:
                l = m+1
            
        
        return False

