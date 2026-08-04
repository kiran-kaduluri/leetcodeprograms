class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        num=set(nums)
        mi,ma=min(nums),max(nums)
        return [x for x in range(mi,ma+1) if  x not in nums]
        