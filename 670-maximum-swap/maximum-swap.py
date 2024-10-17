class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        for i in range(len(digits)):
            max_digit = max(digits[i+1:], default=digits[i])
            if max_digit > digits[i]:
                max_index = ''.join(digits).rfind(max_digit)
                digits[i], digits[max_index] = digits[max_index], digits[i]
                return int(''.join(digits))
        return num
