class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        i = 0
        #phase 1: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # p must not be at start or end
        if i == 0 or i == n - 1:
            return False


        # phase 2: strictly decreasing 
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1

        # q must be after p and not at end
        if j == i or j == n - 1:
            return False
        # phase 3: strictly increasing
        while j + 1 < n and nums[j] < nums[j + 1]:
            j += 1

        # must reach end
        return j == n - 1    

        