class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        def dfs(i: int,num: int):
            if num > high:
                return
            if num >= low:
                ans.append(num)
            if i > 9:
                return
            dfs(i + 1,num * 10 + i)
        for i in range(1,10):
            dfs(i+1,i)
        ans.sort()
        return ans