# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        curr = slow.next
        slow.next=None
        p=None
        n=None
        while curr:
            n=curr.next
            curr.next=p
            p=curr
            curr=n
        f = head
        s = p
        while s:
            fn = f.next
            sn = s.next
            f.next=s
            s.next=fn
            f=fn
            s=sn
        