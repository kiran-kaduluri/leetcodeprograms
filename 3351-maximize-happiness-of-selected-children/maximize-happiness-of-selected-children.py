class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        maxi=0
        for i in range(k):
            l=happiness[i]-i
            if l <= 0:
                break
            maxi += l
        return maxi        
        