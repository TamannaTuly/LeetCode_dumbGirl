# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        root_left = 0
        root_right = 0

        if root == None or (root.left == None and root.right == None):
            return 1
        else:
            if root.left != None:
                root_left = root.left.val
            if root.right != None:
                root_right = root.right.val
            if (root.val == (root_left + root_right)):
                return 1
            else:
                return 0

