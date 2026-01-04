class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        
        for n in nums:
            cnt = 0
            s = 0
            d = 1
            
            while d * d <= n:
                if n % d == 0:
                    cnt += 1
                    s += d
                    if d != n // d:
                        cnt += 1
                        s += n // d
                if cnt > 4:
                    break
                d += 1
            
            if cnt == 4:
                ans += s
        
        return ans
        