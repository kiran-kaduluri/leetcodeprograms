class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = bin(n)[2:]
        lst = [int(bit) for bit in a]
        for i in range(0,len(lst)-1):
            if lst[i] == lst[i+1]:
                return False
        return True    


        