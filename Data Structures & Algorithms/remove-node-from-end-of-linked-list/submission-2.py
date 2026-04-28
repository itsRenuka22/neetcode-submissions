# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def helper(head):
            if not head:
                return (None, 0)
            
            next_node, dist = helper(head.next)
            dist += 1

            if dist == n:
                return (next_node, dist)
            
            head.next = next_node
            return (head, dist)
        
        new_list, d = helper(head)
        return new_list
        