class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_of_nums = len(nums)
        prefix = [1] * num_of_nums
        suffix = [0] * num_of_nums
        result = [0] * num_of_nums
        prefix[0] = 1
        suffix[num_of_nums - 1] = 1

        for i in range(1, num_of_nums):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(num_of_nums - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(num_of_nums):
            result[i] = prefix[i] * suffix[i]
        
        print(prefix, suffix)
        
        return result