class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen=[-1,-1,-1]
        cnt=0
        for i, char in enumerate(s):
            lastseen[ord(char) - ord('a')] = i
            if -1 not in lastseen:
                cnt += 1 + min(lastseen)
        return cnt
        