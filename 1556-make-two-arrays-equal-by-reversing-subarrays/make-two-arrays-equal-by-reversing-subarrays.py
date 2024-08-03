class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a=sorted(arr)
        b=sorted(target)
        return b == a  