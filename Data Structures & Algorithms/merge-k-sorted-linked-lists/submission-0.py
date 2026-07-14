# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        op_list = []
        for ll in lists:
            curr = ll
            while curr is not None:
                op_list.append(curr.val)
                curr=curr.next

        op_list.sort()
        op_ll = ListNode(-1)
        op_curr = op_ll
        for num in op_list:
            op_curr.next = ListNode(num)
            op_curr = op_curr.next

        return op_ll.next