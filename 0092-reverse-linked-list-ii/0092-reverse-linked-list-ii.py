# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy =  ListNode(0, head)
        #Traverse till the left
        leftprev, curr = dummy, head
        for i in range(left-1):
            leftprev, curr = curr, curr.next

        #Reverse the left till right
        prev = None
        for i in range(right-left+1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        #connect the left to leftprev(head) and right to the curr node(next to right)
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next