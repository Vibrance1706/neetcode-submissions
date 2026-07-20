# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        tree = [root]
        while tree:
            node_tree = tree.pop()
            if not node_tree:
                continue

            if node_tree.val == subRoot.val:
                compare_tree = [(node_tree, subRoot)]
                while compare_tree:
                    node_1, node_2 = compare_tree.pop()
                    if not node_1 and not node_2:
                        continue
                    
                    if (not node_1 or not node_2) or node_1.val != node_2.val:
                        break

                    compare_tree.append((node_1.left, node_2.left))
                    compare_tree.append((node_1.right, node_2.right))

                else:
                    return True

            tree.append(node_tree.left)
            tree.append(node_tree.right)

        return False


        
