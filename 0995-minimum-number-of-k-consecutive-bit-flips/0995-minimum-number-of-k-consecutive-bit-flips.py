class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        isFlipped=[0]*n
        flip=0
        ans=0
        for i in range(n):
            if i >= k:
                flip ^= isFlipped[i-k]
            if nums[i] ^ flip == 0:
                if i + k > n:
                    return -1
                isFlipped[i] = 1
                flip ^= 1
                ans += 1
        return ans                
        