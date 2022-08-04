# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def rev(head):
    prev,nextt = None,None
    curr = head
    while curr:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    return prev

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return 1
        
        slow = fast= head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast=fast.next.next
        dummy = head
        slow= rev(slow.next)
        # slow = slow.next
        while slow:
            if dummy.val==slow.val:
                slow=slow.next
                dummy = dummy.next
            else:
                return 0
        return 1
        