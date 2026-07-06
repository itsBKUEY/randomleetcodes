class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while(l<=r):
            m = (l+r)//2

            print(m*m, x)
            if(m*m == x):
                return m
            elif(m*m > x):
                print(">")
                r = m-1
            else:
                print("<")
                l = m+1
                
        return r