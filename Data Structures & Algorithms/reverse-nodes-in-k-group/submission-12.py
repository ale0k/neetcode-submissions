# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = None
        index = 1
        node = master_node = head
        prev = None
        while master_node:
            master_node = master_node.next
            temp = node.next
            node.next = prev
            prev = node
            node = temp
            if index % k == 0 and index > k:
                last_section_end.next = prev
            if index % k == 0:
                if index == k:
                    res = prev
                last_section_end = head
                head = node
                prev = None
            index += 1
        if prev:
            node = prev
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            last_section_end.next = prev
        return res