class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [[0, heights[0]]]
        maxArea = heights[0] 

        for i in range(1, len(heights)):
            #print(stack)
            #print(f'{i}: {maxArea}')
            if stack[-1][1] == heights[i]:
                continue

            while stack and stack[-1][1] > heights[i]:
                temp = stack.pop()
                area = (i-temp[0]) * temp[1]
                maxArea = max(area, maxArea)
            
            j = i

            while heights[i] < heights[j-1] and j > 0:
                j -= 1
            
            stack.append([j, heights[i]])

        print(f'end: {stack}')
        while stack:
            temp = stack.pop()
            area = (len(heights) - temp[0]) * temp[1]
            maxArea = max(area, maxArea)

        return maxArea