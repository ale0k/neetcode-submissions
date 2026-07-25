class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            index = i
            while stack and heights[i] < stack[-1][1]:
                index, last_height = stack.pop()
                max_area = max(max_area, (i - index) * last_height)

            stack.append((index, heights[i]))
            
        while stack:
            index, last_height = stack.pop()
            max_area = max(max_area, (len(heights) - index) * last_height)
        
        return max_area