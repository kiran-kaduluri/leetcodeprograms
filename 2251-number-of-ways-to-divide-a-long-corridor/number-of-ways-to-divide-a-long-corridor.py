class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        
        # If seats are not even or no seats
        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0
        
        ways = 1
        
        # Process seat pairs
        for i in range(2, len(seats), 2):
            # Number of plants between two seat pairs
            gap = seats[i] - seats[i - 1]
            ways = (ways * gap) % MOD
        
        return ways
        