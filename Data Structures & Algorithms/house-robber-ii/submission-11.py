class Solution:
    def __init__(self):
        self.memo = None

    def rob(self, nums: List[int]) -> int:
        self.memo = [[-1, -1] for _ in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        return max(self.dfs(nums, 0, True), self.dfs(nums, 1, False))
        
    def dfs(self, nums, i, flag):
        if i >= len(nums) or (i == len(nums) - 1 and flag == True):
            return 0
        if self.memo[i][flag] != -1:
            rob = self.memo[i][flag]
        else:
            rob = nums[i] + self.dfs(nums, i + 2, flag)
        skip = self.dfs(nums, i + 1, flag or (i == 0))
        self.memo[i][flag] = max(rob, skip)
        return self.memo[i][flag]