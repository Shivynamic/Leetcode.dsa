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
        old = {None:None}
        curr = head
        while curr:
            old[curr] = Node(curr.val)
            curr = curr.next
        
        new = head
        while new:
            copy = old[new]
            copy.next = old[new.next]
            copy.random = old[new.random]
            new=new.next
        return old[head]