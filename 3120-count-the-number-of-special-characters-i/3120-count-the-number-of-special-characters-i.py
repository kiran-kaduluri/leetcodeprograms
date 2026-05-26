class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper=set()
        lower=set()
        for i in word:
            if 'A' <= i <= 'Z':
                upper.add(i)
            else:
                lower.add(i.upper())
        c=0
        for i in upper:
            if i in lower:
                c+=1
        return c        
        
        