# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        val_list = []
        curr = head
        while curr is not None:
            val_list.append(curr.val)
            curr = curr.next
        
        val_list.reverse()
        n_rem = n-1
        val_list.pop(n_rem)
        val_list.reverse()
        
        new_head = ListNode(-1)
        curr = new_head
        for val in val_list:
            curr.next = ListNode(val)
            curr = curr.next

        return new_head.next
