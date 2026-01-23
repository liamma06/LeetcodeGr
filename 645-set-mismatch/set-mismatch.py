class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen= []
        duplicate = 0

        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate = nums[i]
            seen.append(nums[i])

        for i in range(len(nums)):
            if i+1 not in seen:
                return [duplicate,i+1]

        
