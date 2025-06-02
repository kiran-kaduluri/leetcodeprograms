class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        graph = defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        leaves = deque([node for node in graph if len(graph[node])==1])
        
        while n > 2:
            n -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                adjacent = graph[leaf].pop()
                graph[adjacent].remove(leaf)
                if len(graph[adjacent]) == 1:
                    leaves.append(adjacent)

        return list(leaves)
        