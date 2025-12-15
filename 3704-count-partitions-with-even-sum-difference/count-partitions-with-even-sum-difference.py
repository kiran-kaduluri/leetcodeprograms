class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ts=sum(nums)
        ls=0
        c=0

        for i in range(len(nums)-1):
            ls += nums[i]
            rs = ts - ls

            if (ls % 2 ) == (rs % 2 ):
                c+=1
        return c    

        