"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        itr = front = head
        while itr:
            front = itr.next
            
            copy = Node(itr.val)
            itr.next = copy
            copy.next = front
            
            itr = front
        
        itr = head
        while itr:
            if itr.random:
                itr.next.random = itr.random.next
            itr = itr.next.next
        
        itr = head
        dummy = Node(0)
        copy = dummy
        
        while itr:
            front = itr.next.next
            copy.next = itr.next
            copy = copy.next
            itr.next = front
            itr = front
        
        return dummy.next
        
            
        
#         old = {None:None}
#         curr = head
#         while curr:
#             old[curr] = Node(curr.val)
#             curr = curr.next
        
#         new = head
#         while new:
#             copy = old[new]
#             copy.next = old[new.next]
#             copy.random = old[new.random]
#             new=new.next
#         return old[head]