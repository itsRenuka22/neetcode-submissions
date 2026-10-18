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
        dummy = Node(0)
        curr = dummy
        mapping = dict()
        og = head

        while og:
            curr.next = Node(og.val)
            curr = curr.next
            mapping[og] = curr
            og = og.next
        
        copy = dummy.next

        while head:
            if head.random == None:
                copy.random = None
            else:
                copy.random = mapping[head.random]
            head = head.next
            copy = copy.next
        
        return dummy.next
        