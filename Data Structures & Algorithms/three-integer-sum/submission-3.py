class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if sorted_nums[i] + sorted_nums[l] + sorted_nums[r] == 0:
                    trip = [sorted_nums[i], sorted_nums[l], sorted_nums[r]]
                    if trip not in res:
                        res.append(trip)
                    l += 1
                elif sorted_nums[i] + sorted_nums[l] + sorted_nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return res