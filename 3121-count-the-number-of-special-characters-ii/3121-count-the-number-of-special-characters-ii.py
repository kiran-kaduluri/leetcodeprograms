class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in word and ch.upper() in word:
                if word.rfind(ch) < word.find(ch.upper()):
                    c += 1
        return c