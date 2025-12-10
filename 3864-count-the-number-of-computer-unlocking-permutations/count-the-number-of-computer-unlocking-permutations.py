from typing import List
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        root = complexity[0]
        for i in range(1, n):
            if complexity[i] <= root:
                return 0
        ans = 1
        for k in range(1, n):   # computes (n-1)! % MOD
            ans = ans * k % MOD

        return ans
        