class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        P=list(zip(heights,names))
        P.sort(reverse=True, key=lambda x: x[0])
        S=[name for height, name in P]
        return S
