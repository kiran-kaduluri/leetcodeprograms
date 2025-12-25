class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]    
        for i in range(0,numRows - 1):
            prev_row = res[-1]
            cur_row = [1]
            for j in range(len(prev_row)-1):
                cur_row.append(prev_row[j] + prev_row[j+1])
            cur_row.append(1)
            res.append(cur_row)
        return res        
        
        