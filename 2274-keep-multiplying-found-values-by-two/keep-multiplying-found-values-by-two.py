class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        for i in range(0,len(nums)+1):
            if original in nums:
                original = 2 * original
            else:
                return original

        