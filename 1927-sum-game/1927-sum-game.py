class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        lsum=rsum=0
        lques=rques=0
        for i,ch in enumerate(num):
            if ch == '?':
                if i < n//2:
                    lques+=1
                else:
                    rques+=1
            else:
                if i < n//2:
                    lsum+=int(ch)
                else:
                    rsum+=int(ch)
        if (lques-rques) % 2 == 1:
            return True
        return lsum-rsum != (rques-lques)*9 // 2       