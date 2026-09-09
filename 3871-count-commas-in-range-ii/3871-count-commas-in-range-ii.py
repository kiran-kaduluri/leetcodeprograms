class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        thres=1000
        while thres <= n:
            ans += n - thres + 1
            thres *= 1000
        return ans
        