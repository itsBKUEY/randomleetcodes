class Solution:

    #7*1
    #which one is smaller -sized
    #more one to the right
    #6*6

    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights)-1
        largeArea = 0

        while(l<r):
            if(heights[l] > heights[r]):
                length = heights[r]
                right = True
            else:
                length = heights[l]
                right = False

            width = r-l

            area = length*width

            largeArea = max(largeArea, area)
            if(right):
                r -= 1
            else:
                l += 1
        
        return largeArea
            



