class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt=0
        for i in costs:
            if coins >= i:
                coins -= i
                cnt += 1
            else:
                break
        return cnt

        