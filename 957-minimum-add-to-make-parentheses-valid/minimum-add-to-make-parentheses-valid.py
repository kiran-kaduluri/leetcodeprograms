class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op=0
        mi=0
        for c in s:
            if c == '(':
                op += 1
            elif op > 0 :
                op -= 1
            else:
                mi += 1
        return op+mi                


        