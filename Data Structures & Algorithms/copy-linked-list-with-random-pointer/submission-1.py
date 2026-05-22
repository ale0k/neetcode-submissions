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
        if head == None:
            return None
        dummy = copy = Node(0)
        node = head
        index = 0
        hash_map = {}
        while node:
            hash_map[node] = index
            hash_map[index] = copy
            node = node.next
            if node:
                copy.next = Node(0)
                copy = copy.next
            index += 1

        node = head
        copy = dummy
        while node:
            copy.val = node.val
            if node.random:
                copy.random = hash_map[hash_map[node.random]]
            else:
                copy.random = None
            node = node.next
            copy = copy.next
        
        return dummy