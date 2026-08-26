class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        result[len(temperatures)-1] = 0

        stack = []

        for i in range(0, len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                item = stack.pop()
                result[item] = i - item
                
            stack.append(i)
        return result