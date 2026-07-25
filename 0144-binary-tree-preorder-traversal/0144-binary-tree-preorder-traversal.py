# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def insert(root,x):
    if root is None:
        return TreeNode(x)
    if x<root.val:
        root.left=insert(root.left,x)
    else:
        root.right=insert(root.right,x)
    return root
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root is None:
            return ans
        ans.append(root.val)
        ans.extend(self.preorderTraversal(root.left))
        ans.extend(self.preorderTraversal(root.right))
        return ans
        