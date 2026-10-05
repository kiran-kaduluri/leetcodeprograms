class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        sc=deep=0
        for i in range(len(s)):
            if s[i] =='(':
                deep+=1
            else:
                deep-=1
                if s[i-1] == '(':
                    sc +=1 << deep
        return sc

        