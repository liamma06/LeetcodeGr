class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = set()

        for num in nums:
            if num in n :
                return True 
            else:
                n.add(num)

        return False
