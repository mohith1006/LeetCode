class Solution:
    def climbStairs(self, n: int) -> int:
        m={}
        def way(n):
            if n in m:
                return m[n]
            if n==1 or n==2:
                return n
            m[n]=way(n-1)+way(n-2)
            return m[n]
        return way(n)
        
        