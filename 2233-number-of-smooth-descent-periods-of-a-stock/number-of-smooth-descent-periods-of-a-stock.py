class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        c=1
        r=1
        for i in range(1,len(prices)):
            if prices[i - 1] - prices[i] == 1:
                c+=1
            else:
                c=1
            r += c

        return  r               



        