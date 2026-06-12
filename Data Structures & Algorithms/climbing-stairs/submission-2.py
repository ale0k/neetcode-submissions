class Solution:
    def __init__(self):
        self.stair_map = {}

    def climbStairs(self, n: int) -> int:
        if n in self.stair_map:
            return self.stair_map[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.stair_map[n] = res
        return res