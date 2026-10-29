class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        t=[]
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] == target:
                t.append(i)
        return t
        