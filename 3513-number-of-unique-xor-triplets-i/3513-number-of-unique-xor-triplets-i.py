class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        if n == 2: return 2
        p=1
        while p * 2 <= n:
            p *= 2
        return p * 2

        