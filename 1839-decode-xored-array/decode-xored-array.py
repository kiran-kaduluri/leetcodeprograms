class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l=[]
        l.append(first)
        for i in range(len(encoded)):
            l.append(l[len(l)-1]^encoded[i])
        return l    

