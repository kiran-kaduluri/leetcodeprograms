class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        # from left
        for i in range(n):
            if colors[i] != colors[n-1]:
                ans1=n-1-i
                break

        #from right
        for i in range(n-1,-1,-1):
            if colors[i] != colors[0]:
                ans2=i
                break
        return max(ans1,ans2)           
        