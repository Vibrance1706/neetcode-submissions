# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        op_list = []
        tree = [root]
        i=0
        while i<len(tree):
            level = []
            level_size = len(tree)-i
            for _ in range(level_size):
                root = tree[i]
                i+=1

                level.append(root.val)

                if root.left:
                    tree.append(root.left)

                if root.right:
                    tree.append(root.right)

            op_list.append(level)
            
        return op_list