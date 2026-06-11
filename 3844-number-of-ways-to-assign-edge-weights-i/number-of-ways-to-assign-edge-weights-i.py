class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges)+1
        adj = [[] for _ in range(n + 1)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        from collections import deque
        q = deque([(1,0)])
        vis={1}
        max_depth=0
        while q:
            node,depth=q.popleft()
            max_depth=max(max_depth, depth)
            for nei in adj[node]:
                if nei not in vis:
                    vis.add(nei)
                    q.append((nei,depth+1))
    
        return pow(2,max_depth - 1, MOD)