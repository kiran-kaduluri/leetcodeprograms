class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c=dep=0
        for i in range(len(s)):
            if s[i] =='(':
                dep+=1
            elif s[i] == ')' and dep>0:
                dep-=1
            else:
                c+=1
        return c+dep
        