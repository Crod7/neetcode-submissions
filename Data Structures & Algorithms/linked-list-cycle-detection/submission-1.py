# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list1 = head
        list2 = head

        while list2:
            list2 = list2.next
            if list2:
                list2 = list2.next
                
            list1 = list1.next
            
            if list2 and list1.val == list2.val:
                return True
        return False