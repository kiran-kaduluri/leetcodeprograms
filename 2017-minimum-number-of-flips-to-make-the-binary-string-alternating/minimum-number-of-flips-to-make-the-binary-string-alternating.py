class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        s = s + s
        ans = n
        diff1 = diff2 = 0
        l =0
        for i in range(len(s)):
            if s[i] != '01'[i % 2]: diff1 += 1
            if s[i] != '10'[i % 2]: diff2 += 1

            if i - l + 1 > n:
                if s[l] != '01'[l % 2]: diff1 -= 1
                if s[l] != '10'[l % 2]: diff2 -= 1
                l += 1
            if i - l +1 == n:
                ans = min(ans,diff1,diff2)
        return ans            

        