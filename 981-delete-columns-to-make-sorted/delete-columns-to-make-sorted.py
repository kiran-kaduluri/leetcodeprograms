class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        for i in range(len(strs[0])):
            last = 'a'

            for le in strs:
                if le[i] < last:
                    c +=1
                    break
                last = le[i]
        return c           
        