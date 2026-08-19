class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                a, b = stack.pop()
                maxArea = max(maxArea, (index - a) * b)
                start = a
            stack.append((start, height))        
        l = len(heights)
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, h * (l - i))
        return maxArea