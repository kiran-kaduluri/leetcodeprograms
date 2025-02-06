class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=''.join(map(str,digits))
        b=int(a)
        c=b+1
        d=list(str(c))
        e=[int(i) for i in d]
        return e 
        