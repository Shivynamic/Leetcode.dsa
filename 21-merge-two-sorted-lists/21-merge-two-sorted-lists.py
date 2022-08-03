# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1,h2 = list1,list2
        if h1==None:
            return h2
        if h2==None:
            return h1
        if h1.val>h2.val:
            h1,h2 = h2,h1
        head = h1
        
        while h1 and h2:
            temp = None
            while h1 and h1.val<=h2.val:
                temp = h1
                h1 = h1.next
            
            temp.next = h2
            h1,h2 = h2,h1
        return head
        
        
                