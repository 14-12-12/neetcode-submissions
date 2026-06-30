class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)} # enumerate the inorder indices to find and go left and right

        self.pre_idx = 0
        def dfs(l, r): # intially 0, len(inorder)(4)
            if l > r:
                return None # none, none, none none

            root_val = preorder[self.pre_idx] # 1 , 2, 3,4
            self.pre_idx += 1 # 0,1,2,3
            root = TreeNode(root_val) # tree = 1, 2 , 3, 4
            mid = indices[root_val] # 1, 0,2,3
            root.left = dfs(l, mid - 1) # dfs(0,0) - returned 2, dfs(2,1) , dfs(3,2)
            root.right = dfs(mid + 1, r) #dfs(2,3) - dfs(3,3), dfs(4,2)
            return root 

        return dfs(0, len(inorder) - 1)