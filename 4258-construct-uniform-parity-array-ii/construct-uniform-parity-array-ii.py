class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini=min(nums1)
        if mini % 2 == 1:
            return True
        return all(i % 2 == 0 for i in nums1)