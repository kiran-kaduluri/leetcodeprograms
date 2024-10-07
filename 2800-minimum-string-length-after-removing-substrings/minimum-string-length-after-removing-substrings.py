class Solution:
    def minLength(self, s: str) -> int:
        t =[]
        for c in s:
            if t and t[-1] == 'A' and c == 'B':
                t.pop()
            elif t and t[-1] == 'C' and c == 'D':
                t.pop()
            else:
                t +=c
        return len(t)                