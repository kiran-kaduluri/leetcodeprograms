class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        med=nums[len(nums)//2]
        move=0
        for i in nums:
            move+=abs(i-med)
        return move