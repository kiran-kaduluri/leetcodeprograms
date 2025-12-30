class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r=nums[0]
        tot=0
        for i in nums:
            if tot < 0:
                tot = 0
            tot += i
            r = max(r,tot)
        return r        

        