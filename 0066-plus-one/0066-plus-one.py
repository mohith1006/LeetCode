class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=int("".join(map(str,digits)))
        ans+=1
        return list(map(int,str(ans)))

               
        