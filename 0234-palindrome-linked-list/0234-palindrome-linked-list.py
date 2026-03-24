# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        p = None
        n = None
        while curr:
            n = curr.next
            curr.next=p
            p = curr
            curr = n
        curr1 = head
        curr2 = p
        while curr2:
            if curr1.val!=curr2.val:
                return False
            curr1=curr1.next
            curr2=curr2.next
        return True


