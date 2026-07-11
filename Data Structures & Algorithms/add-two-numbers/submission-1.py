# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str, l2_str = '', ''
        
        curr_l1 = l1
        while curr_l1 is not None:
            l1_str+=str(curr_l1.val)
            curr_l1 = curr_l1.next

        curr_l2 = l2
        while curr_l2 is not None:
            l2_str+=str(curr_l2.val)
            curr_l2 = curr_l2.next

        l1_str, l2_str = l1_str[::-1], l2_str[::-1]
        l1_num, l2_num = int(l1_str), int(l2_str)
        total = l1_num + l2_num
        total_str = str(total)

        op_ll = ListNode(-1)
        curr_op = op_ll
        for val in reversed(total_str):
            curr_op.next = ListNode(int(val))
            curr_op = curr_op.next
        

        return op_ll.next