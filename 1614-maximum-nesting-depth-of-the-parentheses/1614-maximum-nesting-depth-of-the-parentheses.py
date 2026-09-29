class Solution:
    def maxDepth(self, s: str) -> int:
        a=0
        cnt=0
        for i in s:
            if i =="(":
                cnt+=1
            elif i == ")":
                cnt-=1
            a=max(a,cnt)
        return a
        