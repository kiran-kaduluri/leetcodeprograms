class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        c={}
        left=0
        max_len=0
        for i in range(len(s)):
            char =s[i]
            c[char] =c.get(char, 0) + 1
            while c[char] > 2:
                c[s[left]] -= 1
                left += 1
            max_len=max(max_len, i - left + 1)
        return max_len
        