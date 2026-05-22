# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_string = ''
        l2_string = ''

        cur = l1
        while cur:
            l1_string = str(cur.val) + l1_string
            cur = cur.next
        
        cur = l2
        while cur:
            l2_string = str(cur.val) + l2_string
            cur = cur.next

        sum_of_nodes = int(l1_string) + int(l2_string)
        string_sum = str(sum_of_nodes)

        dummy = node = ListNode()
        for i in range(len(string_sum) - 1, -1, -1):
            print(string_sum[i])
            string = string_sum[i]
            node.val = int(string) 
            if i > 0:
                node.next = ListNode()
            node = node.next

        return dummy
            