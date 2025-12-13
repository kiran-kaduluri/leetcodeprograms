class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        result = {b: [] for b in order}

        for i in range(len(code)):
            if (isActive[i] and
            businessLine[i] in order and
            code[i] and
            all(c.isalnum() or c == '_' for c in code[i])):
            
                result[businessLine[i]].append(code[i])

        ans = []
        for b in order:
            ans += sorted(result[b])

        return ans