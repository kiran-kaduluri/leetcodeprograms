class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen=set()
        res=[]
        for i in nums:
            if i in seen:
                res.append(i)
            else:
                seen.add(i)
        return res