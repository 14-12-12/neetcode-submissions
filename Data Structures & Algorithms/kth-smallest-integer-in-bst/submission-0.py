# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.arr = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        self.kthSmallest(root.left,k)
        self.arr.append(root.val)
        self.kthSmallest(root.right,k)
        if (len(self.arr)>=k):
            return self.arr[k-1]
            