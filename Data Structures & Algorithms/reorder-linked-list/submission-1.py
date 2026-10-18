# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. Find middle with slow and fast
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #2. Reverse second half
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #3. Merge two lists
        h1 = head
        h2 = prev

        while h2:
            nxt1 = h1.next
            nxt2 = h2.next
            h1.next = h2
            h2.next = nxt1
            h2 = nxt2
            h1 = nxt1