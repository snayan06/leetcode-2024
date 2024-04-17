# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detects the node where the cycle begins in a given singly-linked list.

        Intuition:
        - We use the "two pointers" approach to detect the cycle, similar to Floyd's Tortoise and Hare algorithm.
        - If there's a cycle, both pointers eventually meet somewhere inside the cycle.
        - After detecting the cycle, we reset one pointer to the head and advance both pointers at the same pace.
        - The point where they meet again is the node where the cycle begins.

        Time Complexity: 
        - The time complexity is O(n), where n is the number of nodes in the linked list.
        - In the worst case, both pointers traverse the list once before meeting.

        Space Complexity: 
        - The space complexity is O(1), constant space, as we only use two pointers.

        Args:
        - head: A reference to the head node of the linked list.

        Returns:
        - The node where the cycle begins, if a cycle is detected. Otherwise, returns None.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        return None
