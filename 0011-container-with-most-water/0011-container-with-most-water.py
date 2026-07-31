class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        mx=0
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            car=h*w
            if car>mx:
                mx=car
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return mx