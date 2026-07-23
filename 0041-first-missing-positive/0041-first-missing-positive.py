class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i>0:
                h[i]=1
        ans=1
        while ans in h:
            ans+=1
        return ans
        