# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dum = p_left = p_right = ListNode(0)
        dum.next = head
        l = r = head
        
        for i in range(k-1):
            p_left = l
            l= l.next
        
        nul_check = l
        while nul_check.next:
            p_right = r
            r= r.next
            nul_check = nul_check.next
        
        if l == r:
            return head
        
        p_left.next = r
        p_right.next = l
        r.next , l.next= l.next , r.next
        
        return dum.next