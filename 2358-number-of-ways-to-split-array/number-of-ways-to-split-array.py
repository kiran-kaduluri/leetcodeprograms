class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        li,ri,c=0,sum(nums),0
        for i in range(len(nums)-1):
            li+=nums[i]
            ri-=nums[i]
            if li>=ri:
                c+=1
        return c
        