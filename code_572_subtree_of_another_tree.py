# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isMatching(tree1, tree2):
            if (tree1 and not tree2) or (tree2 and not tree1):
                return False
            if not tree1 and not tree2:
                return True

            if tree1.val == tree2.val:
                if isMatching(tree1.left, tree2.left) and isMatching(tree1.right, tree2.right):
                    return True
                return False
        
        if isMatching(root, subRoot):
            return True
        
        if not root:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
