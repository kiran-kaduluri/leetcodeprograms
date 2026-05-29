class Solution:
    def minElement(self, nums: List[int]) -> int:
        digit_sum=[]
        for i in nums:
            sum1 = 0
            while i > 0:
                sum1 += i%10
                i //= 10
            digit_sum.append(sum1)
        return min(digit_sum)  

        