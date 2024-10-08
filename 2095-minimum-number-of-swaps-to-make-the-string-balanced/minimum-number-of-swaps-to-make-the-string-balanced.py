class Solution:
    def minSwaps(self, s: str) -> int:
        a=0
        for c in s:
            if c == '[':
                a+=1
            elif a > 0 :
                a-=1
        return (a+1)//2        
