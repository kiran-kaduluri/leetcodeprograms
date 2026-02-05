class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            x = nums[i]
            new_index = (i + x) % n
            res.append(nums[new_index])

        return res   
        