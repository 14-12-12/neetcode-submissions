
class Solution:
    def __init__(self):

        self.bool1 = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if not node:
                return 0
            left_h = getHeight(node.left)
            right_h = getHeight(node.right)
            if abs(left_h - right_h) > 1:
                self.bool1 = False
            return max(left_h, right_h) + 1 # final height of the entire
        
        getHeight(root)
        return self.bool1