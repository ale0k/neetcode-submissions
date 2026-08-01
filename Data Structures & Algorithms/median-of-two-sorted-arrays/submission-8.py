class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        total_nums = len(nums1) + len(nums2)
        even = (total_nums % 2) == 0
        res_arr = []

        if even:
            nums_to_discard = (total_nums // 2) - 1
            target_arr_len = 2
        else:
            nums_to_discard = total_nums // 2
            target_arr_len = 1

        while nums_to_discard > 0:
            if i < len(nums1):
                if j >= len(nums2) or nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            else:
                j += 1

            nums_to_discard -= 1
        
        while len(res_arr) < target_arr_len:
            if i < len(nums1):
                if j >= len(nums2) or nums1[i] < nums2[j]:
                    res_arr.append(nums1[i])
                    i += 1
                else:
                    res_arr.append(nums2[j])
                    j += 1

            else:
                res_arr.append(nums2[j])
                j += 1
        
        if even:
            return sum(res_arr) / 2
        else:
            return res_arr[0]

        