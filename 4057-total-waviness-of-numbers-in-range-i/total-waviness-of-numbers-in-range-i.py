class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def wave(num):
            s = str(num)
            n = len(s)
            if n < 3:
                return 0
            c=0
            for i in range(1,n-1):
                if s[i] > s[i -1] and s[i] > s[i + 1]:
                    c +=1
                elif s[i] < s[i -1] and s[i] < s[i + 1]:
                    c +=1
            return c
        ans = 0
        for num in range(num1,num2+1):
            ans += wave(num)
        return ans

        