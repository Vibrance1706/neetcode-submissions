# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i=0
        op_list = []
        op_ll = ListNode(-1)
        curr = head
        while curr is not None:
            op_list.append(curr.val)
            curr = curr.next
        
        op_lis_list = []

        if len(op_list) % k == 0:
            while i < len(op_list):
                counter = 0
                app_list = []
                while counter < k:
                    app_list.append(op_list[i])
                    i+=1
                    counter+=1
            
                op_lis_list.append(app_list)

            reverse_list = []
            for lis in op_lis_list:
                rev_lis = []
                rev_lis = lis[::-1]
                reverse_list.append(rev_lis)

            final_list = []
            for lis in reverse_list:
                for val in lis:
                    final_list.append(val)
            
            op_curr = op_ll
            for num in final_list:
                op_curr.next = ListNode(num)
                op_curr = op_curr.next

            return op_ll.next

        else:
            num_vals = len(op_list) % k
            rem_values = []
            rem_values = op_list[len(op_list)-num_vals:]
            op_list = op_list[0:len(op_list)-num_vals]

            while i < len(op_list):
                counter = 0
                app_list = []
                while counter < k:
                    app_list.append(op_list[i])
                    i+=1
                    counter+=1
            
                op_lis_list.append(app_list)

            reverse_list = []
            for lis in op_lis_list:
                rev_lis = []
                rev_lis = lis[::-1]
                reverse_list.append(rev_lis)

            final_list = []
            for lis in reverse_list:
                for val in lis:
                    final_list.append(val)
            
            for val in rem_values:
                final_list.append(val)

            op_curr = op_ll
            for num in final_list:
                op_curr.next = ListNode(num)
                op_curr = op_curr.next

            return op_ll.next


        

