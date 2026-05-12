class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_width = len(height)
        prefix_max = [0] * max_width
        suffix_max = [0] * max_width
        water = [0] * max_width

        for i in range(1, max_width):
            prefix_max[i] = max(prefix_max[i - 1], height[i - 1])

        for i in range(max_width - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i + 1])

        for i in range(max_width):
            water[i] = max(min(prefix_max[i], suffix_max[i]) - height[i], 0)
        
        return sum(water)