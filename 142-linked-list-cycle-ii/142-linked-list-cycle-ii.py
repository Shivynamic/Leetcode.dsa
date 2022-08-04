# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast= head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
            if slow == fast:
                break
        
        if fast==None or fast.next==None:
            return 
        
        if slow==head:
            while fast.next!=slow:
                fast = fast.next
            return fast.next
        else:
            slow = head
            while slow.next!=fast.next:
                slow=slow.next
                fast=fast.next
            return fast.next
        return -1