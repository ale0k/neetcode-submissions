# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_pointer = ListNode()
        cur_node = None
        while list1 != None or list2 != None:
            if list1 == None:
                if cur_node == None:
                    cur_node = list2
                    head_pointer.next = cur_node
                else:
                    cur_node.next = list2
                    cur_node = cur_node.next
                list2 = list2.next
                
            elif list2 == None:
                if cur_node == None:
                    cur_node = list1
                    head_pointer.next = cur_node
                else:
                    cur_node.next = list1
                    cur_node = cur_node.next
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    if cur_node == None:
                        cur_node = list1
                        head_pointer.next = cur_node
                    else:
                        cur_node.next = list1
                        cur_node = cur_node.next
                    list1 = list1.next
                else:
                    if cur_node == None:
                        cur_node = list2
                        head_pointer.next = cur_node
                    else:
                        cur_node.next = list2
                        cur_node = cur_node.next
                    list2 = list2.next


        return head_pointer.next