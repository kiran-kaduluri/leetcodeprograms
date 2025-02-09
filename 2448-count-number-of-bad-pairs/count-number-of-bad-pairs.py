from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        t=n * (n-1) // 2
        c=0
        f=defaultdict(int)
        for i in range(n):
            d=nums[i]-i
            c+=f[d]
            f[d]+=1
        return t - c    