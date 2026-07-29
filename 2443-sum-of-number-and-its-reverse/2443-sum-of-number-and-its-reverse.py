class Solution:
    def rev(self,x):
        return int(str(x)[::-1])
        
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:
            return True
        for i in range(1,num+1):
            if i+self.rev(i)==num:
                return True
        return False

        