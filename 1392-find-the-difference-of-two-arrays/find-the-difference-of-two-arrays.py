class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        num1d = []
        num2d=[]
        final = []

        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                if nums1[i] not in num1d:
                    num1d.append(nums1[i])
            if nums2[i] not in nums1:
                if nums2[i] not in num2d:
                    num2d.append(nums2[i])

        final.append(num1d)
        final.append(num2d)
        return final
        """
        num1d = []
        num2d = []

        for n in nums1:
            if n not in nums2 and n not in num1d:
                num1d.append(n)

        for n in nums2:
            if n not in nums1 and n not in num2d:
                num2d.append(n)

        return [num1d, num2d]
