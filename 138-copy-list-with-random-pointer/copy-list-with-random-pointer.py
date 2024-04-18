"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_hash = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            node_hash[curr] = copy
            curr = curr.next
        
        curr=head
        while curr:
            node_hash[curr].next = node_hash.get(curr.next)
            node_hash[curr].random = node_hash.get(curr.random)
            curr = curr.next
        
        return node_hash[head]

        