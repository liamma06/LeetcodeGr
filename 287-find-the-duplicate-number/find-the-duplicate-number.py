class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #treat the val as the index to check 

        #find a meeting point (amke sure there is a dup)
        slow = nums[0] 
        fast = nums[nums[0]]

        while slow != fast:
            #keep searching until they match
            slow = nums[slow]
            fast = nums[nums[fast]]

        #find duplicate (where cycle starts) 
        #this works since 
        slow2 = 0 
        while slow2!=slow:
            slow2 = nums[slow2]
            slow= nums[slow]
        return slow 