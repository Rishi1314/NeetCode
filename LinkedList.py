#138 Copy List with Random Pointer
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
        oldToCopy={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            oldToCopy[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=oldToCopy[curr]
            copy.next=oldToCopy[curr.next]
            copy.random=oldToCopy[curr.random]
            curr=curr.next
        return oldToCopy[head]

#2 add two numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            v1= l1.val if l1 else 0
            v2= l2.val if l2 else 0

            val=v1+v2+carry

            carry=val//10
            val=val%10

            curr.next=ListNode(val)
            
            l1= l1.next if l1 else None
            l2= l2.next if l2 else None
            curr=curr.next
        return dummy.next