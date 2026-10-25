# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast, list1 = head, head, head

        # 1. Separation point 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr2 = slow.next
        slow.next = None

        # 2. Reverse second half
        prev = None

        while curr2:
            nxt = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = nxt

        # Now, prev points to start of reversed second half
        list2 = prev

        while list1 and list2:
            nxt1 = list1.next
            nxt2 = list2.next
            list1.next = list2
            list2.next = nxt1
            list2 = nxt2
            list1 = nxt1
        