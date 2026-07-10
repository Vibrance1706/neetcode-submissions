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
        # if head is None:
        #     return None

        # ll_dict = {}
        # curr = head

        # while curr is not None:
        #     if curr.val not in ll_dict:
        #         ll_dict[curr.val] = []
        #         nxt = curr.next

        #         if nxt is None:
        #             ll_dict[curr.val].append(None)
        #         else:
        #             ll_dict[curr.val].append(nxt.val)

        #         rand_head = curr.random

        #         if rand_head == None:
        #             index = None
        #             ll_dict[curr.val].append(index)
        #         else:
        #             rand_ite = head
        #             rand_val = rand_head.val
        #             index = 0
        #             while rand_ite is not None:
        #                 if rand_ite.val == rand_val:
        #                     break
        #                 rand_ite = rand_ite.next
        #                 index +=1
        #             ll_dict[curr.val].append(index)
        
        #     curr = curr.next

        # op_node = Node(-1)
        # new_curr = op_node
        # node_map = {}
        # for key in ll_dict:
        #     new_node = Node(key)
        #     node_map[key] = new_node
        #     new_curr.next = new_node
        #     new_curr = new_curr.next
        
        # new_curr = op_node.next

        # for key in ll_dict:
        #     next_val, rand_index = ll_dict[key]

        #     if next_val is not None:
        #         new_curr.next = node_map[next_val]

        #     if rand_index is not None:
        #         temp = op_node.next
        #         for _ in range(rand_index):
        #             temp = temp.next
        #         new_curr.random = temp

        #     new_curr = new_curr.next

        # return op_node.next
        if head is None:
            return None

        ll_dict = {}
        curr = head

        while curr is not None:
            if curr not in ll_dict:
                ll_dict[curr] = []

                nxt = curr.next
                ll_dict[curr].append(nxt if nxt is not None else None)

                rand_head = curr.random
                ll_dict[curr].append(rand_head if rand_head is not None else None)

            curr = curr.next

        op_node = Node(-1)
        new_curr = op_node
        node_map = {}

        for key in ll_dict:
            new_node = Node(key.val)
            node_map[key] = new_node
            new_curr.next = new_node
            new_curr = new_curr.next

        for key in ll_dict:
            next_val, rand_val = ll_dict[key]

            if next_val is not None:
                node_map[key].next = node_map[next_val]

            if rand_val is not None:
                node_map[key].random = node_map[rand_val]

        return op_node.next




            
                