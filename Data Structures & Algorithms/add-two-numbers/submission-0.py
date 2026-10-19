# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry > 0:
            if not l1 and not l2:
                add = carry
            elif not l1:
                add = 0 + l2.val + carry
                l2 = l2.next
            elif not l2:
                add = l1.val + 0 + carry
                l1 = l1.next
            else:
                add = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            
            node_val = add % 10
            carry = add // 10
            curr.next = ListNode(node_val)
            curr = curr.next
        
        return dummy.next
        