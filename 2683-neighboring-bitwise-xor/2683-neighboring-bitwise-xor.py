class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        i=0
        for j in derived:
            i=i^j
        if i==0:
            return True
        else:
            return False

        