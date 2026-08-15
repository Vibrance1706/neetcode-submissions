# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        val_list = []
        while stack:
            curr = stack.pop()
            val_list.append(curr.val)
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        val_list.sort()
        return val_list[k-1]

    

