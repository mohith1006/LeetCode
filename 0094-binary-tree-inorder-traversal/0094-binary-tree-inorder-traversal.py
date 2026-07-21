# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def insert(root,x):
    if root is None:
        return TreeNode(x)
    if x<root.data:
        root.left=insert(root.left,x)
    else:
        root.right=insert(root.right,x)
    return root
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans
        