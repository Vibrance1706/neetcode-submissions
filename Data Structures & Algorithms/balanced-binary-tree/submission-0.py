# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        stack = [(root, False)]
        heights = {None: 0}
        while stack:
            node, visited = stack.pop()
            if not node:
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left_hei = heights[node.left]
                right_hei = heights[node.right]
                if abs(left_hei - right_hei) > 1:
                    return False
            
                heights[node] = 1+max(left_hei, right_hei)

        return True
            
        
        
