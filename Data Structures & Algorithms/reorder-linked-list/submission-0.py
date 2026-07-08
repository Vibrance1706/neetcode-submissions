# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ll_values = []
        curr = head
        while curr is not None:
            ll_values.append(curr.val)
            curr = curr.next
        
        op_ll = []
        l, r = 0, len(ll_values)-1
        while l <= r:
            if l == r:
                op_ll.append(ll_values[l])
                break

            op_ll.append(ll_values[l])
            op_ll.append(ll_values[r])
            l+=1
            r-=1

        curr = head
        i = 0
        while curr is not None:
            curr.val = op_ll[i]
            curr = curr.next
            i += 1
        

    