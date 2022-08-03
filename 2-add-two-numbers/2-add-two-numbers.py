# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry =0
        
        while l1 or l2 or carry==1:
            summ =0
            if l1:
                summ+=l1.val
                l1= l1.next
            if l2:
                summ+=l2.val
                l2 = l2.next
            
            summ+=carry
            carry = summ//10
            newNode= ListNode(summ%10)
            temp.next = newNode
            temp = temp.next
        return dummy.next
                
                
        
        