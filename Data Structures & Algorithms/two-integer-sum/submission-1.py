class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_before in enumerate(nums):
            for j, num_after in enumerate(nums):
                if i != j:
                    if num_before + num_after == target:
                        return [i, j]