class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(set(nums))
        m=len(nums)
        if n != m :
            return True 
        return False