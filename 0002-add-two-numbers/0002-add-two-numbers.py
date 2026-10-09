# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        node = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            # values at l1 and l2 node
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # sum to get val, eg: 3+5+1 = 12
            val = v1 + v2 + carry
            # get the carry, eg: 12//10 = 1 -> carry
            carry = val // 10
            # ones digit of the number, eg: 12%10 = 2 -> *val at that node*
            val = val % 10

            # Add node
            node.next = ListNode(val)

            # Move the pointers
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
