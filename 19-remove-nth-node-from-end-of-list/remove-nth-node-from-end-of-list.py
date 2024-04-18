# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        # Handle the case when removing the first node
        if n == count:
            return head.next

        curr = head
        count2 = 0
        while curr and curr.next:
            count2 += 1
            if count2 == count - n:
                curr.next = curr.next.next
                break

            curr = curr.next

        return head
