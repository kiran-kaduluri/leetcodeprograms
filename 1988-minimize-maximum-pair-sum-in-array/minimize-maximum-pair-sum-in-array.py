class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        st,en=0,len(nums) - 1
        max_pair=0

        while st<en:
            pair_sum = nums[st] + nums[en]
            max_pair=max(max_pair,pair_sum)
            st += 1
            en -= 1

        return max_pair
        