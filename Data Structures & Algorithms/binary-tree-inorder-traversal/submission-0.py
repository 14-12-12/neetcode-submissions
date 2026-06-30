# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.list1 =[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.list1
        self.inorderTraversal(root.left)
        self.list1.append(root.val)
        self.inorderTraversal(root.right)
        return self.list1

        

    
    


        