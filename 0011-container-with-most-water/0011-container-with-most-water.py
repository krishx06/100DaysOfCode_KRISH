class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            if height[left] < height[right]:
                h = height[left]  
            else:
                h = height[right]
            
            width = right - left
            area = h * width
            
            if area > max_water:
                max_water = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
