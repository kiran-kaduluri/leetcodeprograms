class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        t=sum(nums)
        s=0
        for i in reversed(range(len(nums))):
            s+=nums[i]
            rem=t-s

            if rem > nums[i]:
                return rem + nums[i]

        return -1        
        