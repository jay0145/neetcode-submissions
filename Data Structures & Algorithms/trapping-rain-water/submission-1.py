class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = [0] * len(height)
        r = [0] * len(height)
        l[0] = height[0]
        r[len(height)-1] = height[len(height)-1]

        for i in range(1, len(height)):
            if height[i] > l[i-1]:
                l[i] = height[i]
            else:
                l[i] = l[i-1]

        for i in range(len(height)-2, -1, -1):
            if height[i] > r[i+1]:
                r[i] = height[i]
            else:
                r[i] = r[i+1]

        for i in range(1, len(height)-1):

            area = min(l[i], r[i]) - height[i]
            if area > 0:
                water += area
        
        return water