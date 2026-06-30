# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first half is ordered
        # second half is reversed
        # 1->2,     4->3
        
        first = head.next
        second = head
        while first and first.next:
            second = second.next
            first = first.next.next

        # reset first half
        first = head

        # flip second half in reverse
        curr = second
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev

        # merge 2 linked lists
        while first:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 

        



