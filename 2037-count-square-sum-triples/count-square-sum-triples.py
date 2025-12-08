class Solution:
    def countTriples(self, n: int) -> int:
        sq={i*i for i in range(1,n+1)}
        r=0
        for i in range(1,n+1):
            a=i*i
            for j in range(i+1,n+1):
                c= a + j*j
                
                if c in sq:
                    r+=2        
        return r