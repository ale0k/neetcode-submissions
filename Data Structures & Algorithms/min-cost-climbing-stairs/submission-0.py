class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost_for_step = []
        for i, c in enumerate(cost):
            if i > 1:
                min_cost_for_step.append(min(min_cost_for_step[i - 1], min_cost_for_step[i - 2]) + c)
            else:
                min_cost_for_step.append(c)
        return min(min_cost_for_step[-1], min_cost_for_step[-2])
