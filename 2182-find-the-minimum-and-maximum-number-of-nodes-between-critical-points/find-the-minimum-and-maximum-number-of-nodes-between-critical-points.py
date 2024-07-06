# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        cp_indices = []
        curr = head.next
        prev = head
        index = 1
        while curr and curr.next:
            next_node = curr.next
            # local maxima
            if curr.val > prev.val and curr.val > next_node.val:
                cp_indices.append(index)
            # local minima
            if curr.val < prev.val and curr.val < next_node.val:
                cp_indices.append(index)

            prev = curr
            curr = next_node
            index += 1

        print(cp_indices)
        if len(cp_indices) < 2:
            return [-1, -1]

        min_distance = float("inf")
        for i in range(1, len(cp_indices)):
            min_distance = min(min_distance, cp_indices[i] - cp_indices[i - 1])

        max_distance = cp_indices[-1] - cp_indices[0]
        return [min_distance, max_distance]
