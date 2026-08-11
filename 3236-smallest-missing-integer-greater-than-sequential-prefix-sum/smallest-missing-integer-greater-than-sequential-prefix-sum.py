class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        tsum=nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                tsum+=nums[i]
            else:
                break
        nset=set(nums)
        while tsum in nset:
            tsum+=1
        return tsum                

        