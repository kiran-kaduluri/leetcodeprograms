class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        c=[1]*(n)
        c[0]=0
        c[1]=0
        for i in range(2,n):
            if c[i]:
                for j in range(i*i,n,i):
                    c[j]=0
        return(c.count(1))
        