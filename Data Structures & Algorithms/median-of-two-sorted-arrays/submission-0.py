class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = nums1 + nums2
        list1.sort()

        val = len(list1) / 2

        print(val)
        print(math.floor(val))
        print(math.ceil(val))

        if len(list1) % 2 == 0:
            val1 = ((list1[math.floor(val - 1)] + list1[math.ceil(val)]) / 2)
            return val1
        else:
            return list1[math.floor(val)]
