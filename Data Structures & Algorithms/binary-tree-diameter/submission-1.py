# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_dia = 0
        stack = [root]
        heights = {None:0}

        while stack:
            node = stack[-1]
            if node.left and node.left not in heights:
                stack.append(node.left)
            elif node.right and node.right not in heights:
                stack.append(node.right)
            else:
                stack.pop()
                left = heights[node.left]
                right = heights[node.right]
                max_dia = max(max_dia, left + right)

                heights[node] = 1+max(left, right)
            
        return max_dia
