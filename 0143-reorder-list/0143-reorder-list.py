# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Split using slow and fast
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        second = slow.next
        prev =  None
        slow.next = None #last of the first half should also point to null
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge them 
        first, second = head, prev #second will point to null after the reversal loop
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        