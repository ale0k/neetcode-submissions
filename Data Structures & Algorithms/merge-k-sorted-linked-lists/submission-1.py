# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while True:
            min_node = None
            for i in range(len(lists)):
                cur = lists[i]
                if cur is None:
                    continue
                if min_node:
                    if cur.val <= min_node[0].val:
                        min_node = (cur, i)
                else:
                    min_node = (cur, i)
            if min_node == None:
                break
            else:
                _, index = min_node
                lists[index] = lists[index].next
            node.next = min_node[0]
            node = node.next
        return dummy.next