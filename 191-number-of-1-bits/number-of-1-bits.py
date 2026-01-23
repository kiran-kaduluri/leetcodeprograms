class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        bin_num = str(bin(n))
        for i in bin_num[2:]:
            if int(i)==1:
                count+=1
        return count        
        