class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i, num in enumerate(nums):
            for j, _ in enumerate(result):
                if i != j:
                    result[j] *= num
        return result