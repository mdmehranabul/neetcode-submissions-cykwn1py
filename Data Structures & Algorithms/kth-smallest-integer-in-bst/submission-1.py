# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # Solution 1
        # stack=[]
        # curr=root

        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr=curr.left
        #     curr=stack.pop()
        #     k-=1

        #     if k==0:
        #         return curr.val
        #     curr=curr.right

    # Solution 2
        arr=[]
        def dfs(root):
            if not root: return 

            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)
        return arr[k-1]

