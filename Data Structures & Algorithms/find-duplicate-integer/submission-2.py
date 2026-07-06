class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        temp = 0
        while temp != slow:
            temp = nums[temp]
            slow = nums[slow]
        return slow
            
