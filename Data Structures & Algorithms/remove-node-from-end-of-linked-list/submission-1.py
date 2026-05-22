# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        prev = None
        if head.next == None:
            return

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        node = prev
        after = prev.next
        if n > 1:
            for i in range(n - 1):
                before = node
                node = node.next
                after = node.next
            before.next = after
        else:
            prev = prev.next
        
        
        node = prev
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev