class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        return self.dfs(nums, 0)
        
    def dfs(self, nums, i):
        if i >= len(nums):
            return 0
        if i in self.memo:
            rob = self.memo[i]
        else:
            rob = nums[i] + self.dfs(nums, i + 2)
        skip = self.dfs(nums, i + 1)
        self.memo[i] = max(rob, skip)
        return self.memo[i]