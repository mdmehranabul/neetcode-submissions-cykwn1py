# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q=deque([(root,0)])
        col_dict = defaultdict(list)
        max_col, min_col = 0,0

        while q:
            node, col = q.popleft()
            max_col, min_col = max(max_col, col), min(min_col, col)
            col_dict[col].append(node.val)

            if node.left:
                q.append((node.left,col-1))
            
            if node.right:
                q.append((node.right,col+1))

        return [col_dict[i] for i in range(min_col,max_col+1)]

