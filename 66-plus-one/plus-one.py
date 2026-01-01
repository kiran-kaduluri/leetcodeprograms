class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = int("".join(map(str, digits)))
        t = l + 1
        lst = list(map(int, str(t)))
        return lst

        