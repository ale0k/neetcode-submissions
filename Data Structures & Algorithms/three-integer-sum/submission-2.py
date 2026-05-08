class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        r = len(nums) - 1
        result = []
        sorted_nums = sorted(nums)
        for i, num in enumerate(sorted_nums):
            if num > 0:
                break

            if i > 0 and num == sorted_nums[i - 1]:
                continue
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                threesum = num + sorted_nums[l] + sorted_nums[r]
                if threesum == 0:
                    result.append([num, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                elif num + sorted_nums[l] + sorted_nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return result