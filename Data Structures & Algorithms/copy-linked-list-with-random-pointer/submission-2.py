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
        hash_map = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            hash_map[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = hash_map[cur]
            copy.next = hash_map[cur.next]
            copy.random = hash_map[cur.random]
            cur = cur.next

        return hash_map[head]