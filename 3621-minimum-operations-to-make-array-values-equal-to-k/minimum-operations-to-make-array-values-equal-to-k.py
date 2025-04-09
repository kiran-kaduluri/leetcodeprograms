class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        u=set(nums)
        ue=len(u)

        if k in nums:
            return ue - 1
        else:
            return ue        
        