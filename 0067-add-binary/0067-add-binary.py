class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=list(map(int,a))
        d=list(map(int,b))
        ans1=0
        ans2=0
        for i in c:
            ans1=ans1*2+i
        for j in d:
            ans2=ans2*2+j
        ans=ans1+ans2
        if ans==0:
            return '0'
        res=''
        while ans>0:
            res=str(ans%2)+res
            ans//=2
        return res

        