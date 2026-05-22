# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        iterations = 0
        while fast and slow:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
            if fast == slow and iterations > 0:
                return True
            iterations += 1
    
        return False