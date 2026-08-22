class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits=[int(i) for i in str(n)]
        d=sum(digits)
        prod=1
        for i in digits:
            prod*=i
        t=d+prod
        return t!=0 and n%t==0

        