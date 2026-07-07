class Solution:
    def sumAndMultiply(self, n: int) -> int:
        result = "".join([char for char in str(n) if char != '0'])
        x=sum(int(digit) for digit in str(n))
        if not result:
            return 0
        return int(result) * x
        