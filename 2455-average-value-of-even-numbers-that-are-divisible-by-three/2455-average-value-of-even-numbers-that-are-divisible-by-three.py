class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        c=0
        for i in nums:
            if i % 2==0 and i % 3 == 0:
                s+=i
                c+=1
        return s//c if c > 0 else 0

        