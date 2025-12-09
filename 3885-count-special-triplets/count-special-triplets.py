from collections import Counter
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        r = Counter(nums)  
        l = Counter()
        a = 0
        for x in nums:
            r[x] -= 1  
            target = 2 * x
            a += l[target] * r[target]
            a %= MOD
            l[x] += 1        
        
        return a
        