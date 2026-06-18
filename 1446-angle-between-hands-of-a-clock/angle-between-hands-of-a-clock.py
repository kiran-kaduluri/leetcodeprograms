class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_ang=minutes * 6
        hou_ang=(hour % 12) * 30 + minutes * 0.5
        diff=abs(hou_ang-min_ang)
        return min(diff,360-diff)
        