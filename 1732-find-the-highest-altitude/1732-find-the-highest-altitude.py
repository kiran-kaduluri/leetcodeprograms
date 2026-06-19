class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        hi=[]
        s=0
        for i in range(len(gain)):
            s+=gain[i]
            hi.append(s)
        hi.append(0)
        return max(hi)

            
        