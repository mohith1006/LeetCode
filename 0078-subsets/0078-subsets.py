class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for i in nums:
            new=[]
            for j in ans:
                new.append(j+[i])
            ans.extend(new)

           
        return ans
        