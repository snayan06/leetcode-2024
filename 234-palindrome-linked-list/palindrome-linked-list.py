# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        stack = []
        tmp = head
        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        
        tmp = head
        while tmp:
            if stack[-1] != tmp.val:
                return False
            tmp = tmp.next
            stack.pop()
        
        return True
        