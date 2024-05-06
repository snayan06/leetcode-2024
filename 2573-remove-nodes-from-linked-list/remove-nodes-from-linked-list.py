# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [head]
        head = head.next

        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()

            if stack:
                stack[-1].next = head

            stack.append(head)
            head = head.next

        return stack[0]