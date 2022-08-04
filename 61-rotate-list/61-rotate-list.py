# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next == None or k==0:
            return head
        
        l=1
        temp = curr = head
        while curr.next:
            curr = curr.next
            l+=1
        curr.next = head
        
        k = l-(k%l)-1
        while k and temp.next:
            temp = temp.next
            k-=1
        newHead = temp.next
        temp.next = None
        return newHead
        