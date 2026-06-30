# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_list = []
        def bfs(self, root:Optional[TreeNode]):
            queue = deque()
            if root:
                queue.append(root)
            level = 0
            while(len(queue)>0):
                list1 = []
                for i in range (0, len(queue)):
                    curr = queue.popleft()
                    list1.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level_list.append(list1)
                list_1 = []
                level = level+1
        bfs(self, root)
        return level_list

        



        