# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        root_val = root.val
        traverse = [(root, root_val)]
        count = 0

        while traverse:
            node, present_max = traverse.pop(0)
            if node.val>=present_max:
                count += 1

            new_max = max(present_max, node.val)
            
            if node.left:
                traverse.append((node.left, new_max))
            if node.right:
                traverse.append((node.right, new_max))
        
        return count
