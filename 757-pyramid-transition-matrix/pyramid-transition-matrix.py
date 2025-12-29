class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        
        # Map (left, right) -> possible top blocks
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[a + b].append(c)
        
        # Backtracking to build next row
        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            
            def build_next(i, next_row):
                if i == len(row) - 1:
                    return dfs(next_row)
                
                pair = row[i:i+2]
                if pair not in mp:
                    return False
                
                for ch in mp[pair]:
                    if build_next(i + 1, next_row + ch):
                        return True
                return False
            
            return build_next(0, "")
        
        return dfs(bottom)
        