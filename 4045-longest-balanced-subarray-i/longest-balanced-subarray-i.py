class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            eset=set()
            oset=set()
            for j in range(i,len(nums)):
                if nums[j] % 2 == 0:
                    eset.add(nums[j])
                else:
                    oset.add(nums[j])
                if len(eset) == len(oset):
                    ans = max(ans,j - i +1)
        return ans                      

        