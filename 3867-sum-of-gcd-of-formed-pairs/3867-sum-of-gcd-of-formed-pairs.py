import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        prefix=[]
        cmax=0
        for x in nums:
            if x > cmax:
                cmax=x
            prefix.append(math.gcd(x,cmax))
        prefix.sort()
        tsum=0
        l=0
        r=n-1
        while l < r:
            tsum += math.gcd(prefix[l], prefix[r])
            l += 1
            r -= 1
        return tsum
        