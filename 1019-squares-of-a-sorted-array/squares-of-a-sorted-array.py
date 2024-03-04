class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            lt=i*i
            l.append(lt)
        l.sort()
        return l    


        