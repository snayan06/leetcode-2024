# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to reverse a linked list
        def reverseLinkedList(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Reverse the linked list
        head = reverseLinkedList(head)

        # Initialize carry as 0
        carry = 0
        current = head
        prev = None

        while current:
            # Double the value of the current node and add the carry
            current.val = current.val * 2 + carry
            # Update carry for next node
            carry = current.val // 10
            # Update current node's value to its remainder after dividing by 10
            current.val %= 10

            # Move to the next node
            prev = current
            current = current.next

        # If there's still a carry after processing all nodes, add a new node
        if carry > 0:
            prev.next = ListNode(carry)

        # Reverse the linked list again to get the correct order
        return reverseLinkedList(head)
