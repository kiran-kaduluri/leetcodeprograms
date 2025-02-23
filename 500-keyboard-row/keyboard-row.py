class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res=[]
        for i in words:
            w=set(i.lower())
            if w<=row1 or w<=row2 or w<=row3:
                res.append(i)
        return res       


        