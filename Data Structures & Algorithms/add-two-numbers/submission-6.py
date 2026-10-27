# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1, v2 = l1, l2
        carry = 0
        dummy = ListNode()
        curr = dummy

        while v1 or v2:
            if not v1:
                curr.next = ListNode((v2.val + carry) % 10)
                carry =  (v2.val + carry) // 10
                v2 = v2.next
            elif not v2:
                curr.next = ListNode((v1.val + carry) % 10)
                carry = (v1.val + carry) // 10
                v1 = v1.next
            else:
                curr.next = ListNode((v1.val + v2.val + carry) % 10)
                carry = (v1.val + v2.val + carry) // 10
                v1 = v1.next
                v2 = v2.next
            
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next
        