class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        a=Counter(arr)
        b=dict(sorted(a.items(),key=lambda item : item[1]))
        c=[]
        for i,j in b.items():
            c.extend([i]*j)
        d=[]
        for i in range(k,len(c)):
            d.append(c[i])
        e=Counter(d)
        return len(e)     