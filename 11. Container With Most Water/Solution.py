class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            current_area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, current_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
