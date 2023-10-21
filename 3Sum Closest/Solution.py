class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')
        minDiff = float('inf')
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                currentSum = nums[i]+nums[left]+nums[right]
                diff = abs(currentSum - target)
                if diff < minDiff:
                    minDiff = diff
                    closestSum = currentSum
                if currentSum < target:
                    left += 1
                else:
                    right -= 1
        return closestSum
