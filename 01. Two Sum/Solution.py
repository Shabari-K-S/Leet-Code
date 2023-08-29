from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {} 
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result) 
