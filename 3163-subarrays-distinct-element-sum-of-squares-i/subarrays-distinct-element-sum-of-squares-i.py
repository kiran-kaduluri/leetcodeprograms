class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        for i in range(n):
            d=set()
            for j in range(i,n):
                d.add(nums[j])
                c=len(d)
                s+= c **2
        return s
        