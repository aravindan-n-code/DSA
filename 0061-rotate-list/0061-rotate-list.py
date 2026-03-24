# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or not head:
            return head
        count=1
        temp=head
        while temp.next:
            count +=1
            temp=temp.next
        
        k=k%count
        if k==0:
            return head
        temp.next=head
        s=count-k
        for i in range(s):
            temp=temp.next
        newhead=temp.next
        temp.next=None
        return newhead