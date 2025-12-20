class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=[i for i in range (1,len(nums)+1)]
        s=sum(nums)
        k=len(n)
        n1=k*(k+1)//2
        return n1-s
        