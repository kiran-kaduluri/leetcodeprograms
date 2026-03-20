class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        ans = [[0] * (n-k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals=[]
                for x in range(i,i+k):
                    for y in range(j,j+k):
                        vals.append(grid[x][y])
                vals=sorted(set(vals))

                min_diff = float('inf')
                for p in range(1,len(vals)):
                    min_diff=min(min_diff, vals[p] - vals[p-1])
                ans[i][j] = min_diff if min_diff != float('inf') else 0
        return ans