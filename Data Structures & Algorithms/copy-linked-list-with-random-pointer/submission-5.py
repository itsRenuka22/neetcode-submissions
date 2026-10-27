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
        map = {None: None}
        curr = head

        while curr:
            new = Node(curr.val)
            map[curr] = new
            curr = curr.next

        curr = head
        while curr:
            node = map[curr]
            node.next = map[curr.next]
            node.random = map[curr.random]
            curr = curr.next
        
        return map[head]
        