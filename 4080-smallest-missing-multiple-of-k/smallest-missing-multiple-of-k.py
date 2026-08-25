class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num=set(nums)
        multi=k
        while multi in num:
            multi+=k
        return multi
        