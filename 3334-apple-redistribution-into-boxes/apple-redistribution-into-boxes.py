class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        k=sum(apple)
        capacity.sort(reverse=True)
        for i,c in enumerate(capacity):
            k -= c

            if(k <= 0):
                return i+1

        