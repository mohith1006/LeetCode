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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root is None:
            return ans
        ans.extend(self.postorderTraversal(root.left))
        ans.extend(self.postorderTraversal(root.right))
        ans.append(root.val)
        return ans

        