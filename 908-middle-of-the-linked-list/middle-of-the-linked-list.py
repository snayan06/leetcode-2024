# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a singly-linked list.

        Args:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            Optional[ListNode]: The middle node of the linked list.

        Detailed Explanation:
        - Approach 1: Counting the number of nodes
            - We first traverse the linked list to count the number of nodes.
            - Then, we traverse the linked list again halfway to find the middle node.
            - This approach requires two passes through the entire linked list, making it less efficient.

        - Approach 2: Slow and fast pointers
            - We use the slow and fast pointers technique.
            - We initialize two pointers, 'slow' and 'fast', both pointing to the head of the linked list.
            - We move the 'slow' pointer one step forward and the 'fast' pointer two steps forward in each iteration of the loop.
            - When the 'fast' pointer reaches the end of the list (i.e., becomes 'None'), the 'slow' pointer will be at the middle of the list.
            - This approach only requires a single pass through the list, making it more efficient.

        Time Complexity:
        - Approach 1: O(n), where n is the number of nodes in the linked list.
        - Approach 2: O(n), where n is the number of nodes in the linked list.

        Space Complexity:
        - Approach 1: O(1), as it only uses constant extra space.
        - Approach 2: O(1), as it only uses constant extra space.
        """

        # Approach 1: Counting the number of nodes
        """
        # Count the number of nodes in the linked list
        current = head
        node_count = 0
        while current:
            node_count += 1
            current = current.next

        # Move to the middle node
        current = head
        for _ in range(node_count // 2):
            current = current.next

        return current
        """

        # Approach 2: Slow and fast pointers
        # Initialize slow and fast pointers to the head of the list
        slow = fast = head

        # Move slow and fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # At this point, slow is at the middle
        return slow
