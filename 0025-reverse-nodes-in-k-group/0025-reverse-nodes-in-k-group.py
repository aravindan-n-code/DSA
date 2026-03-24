# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        next_node = dummy
        prev = dummy
        
        count = 0
        while curr.next:
            curr = curr.next
            count += 1
            
        while count >= k:
            curr = prev.next
            next_node = curr.next
            
            for _ in range(k - 1):
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                next_node = curr.next
            
            prev = curr
            count -= k
            
        return dummy.next