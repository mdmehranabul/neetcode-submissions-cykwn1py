# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(curr):
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr= temp
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        carry, head = 0, None

        while l1 or l2 or carry:
            tot = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = tot // 10
            node = ListNode(tot % 10)
            node.next = head
            head = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head








        