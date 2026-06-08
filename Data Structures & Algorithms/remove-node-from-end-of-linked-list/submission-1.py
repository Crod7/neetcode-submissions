# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reverse the list
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # remove the Nth node from the end, by reverseing the list but skipping Nth node
        count = n
        newList = None
        revCurr = prev
        while revCurr:
            count -= 1
            if count == 0:
                revCurr = revCurr.next
                continue
            else:
                temp = revCurr.next

            revCurr.next = newList
            newList = revCurr
            revCurr = temp


        return newList

            
