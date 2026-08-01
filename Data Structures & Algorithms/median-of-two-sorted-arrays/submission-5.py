class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        even = (len(nums1) + len(nums2) % 2) == 0
        combined = []
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    combined.append(nums1[i])
                    i += 1
                else:
                    combined.append(nums2[j])
                    j += 1
            else:
                if i < len(nums1):
                    combined.append(nums1[i])
                    i += 1
                else:
                    combined.append(nums2[j])
                    j += 1
        if len(combined) % 2 == 0:
            return (combined[(len(combined) // 2) - 1] + combined[(len(combined) // 2)]) / 2
        else:
            return combined[len(combined) // 2]
        return 0
