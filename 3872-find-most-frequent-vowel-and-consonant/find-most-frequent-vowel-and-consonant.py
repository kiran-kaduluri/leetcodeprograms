class Solution:
    def maxFreqSum(self, s: str) -> int:
        c=0
        v=0
        d=set(s)
        for i in d:
            if i in "aeiou":
                v = max(v,s.count(i))
            else:
                c= max(c,s.count(i))
        return c+v            








        