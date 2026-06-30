# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        list_levels = []
        def bfs_right(self, root):
            queue = deque()
            if root:
                queue.append(root)
            level = 0
            while (len(queue)>0):
                list_1 = []
                for i in range (0, len(queue)):
                    curr = queue.popleft()
                    list_1.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level = level+1
                list_levels.append(list_1[len(list_1)-1])
                list_1 = []
        bfs_right(self,root)
        return list_levels


        