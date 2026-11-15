# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        qu = collections.deque([root])
        res = []

        while qu:
            rightSide = None
            for _ in range(len(qu)):
                node = qu.popleft()

                if node:
                    rightSide = node
                    qu.append(node.left)
                    qu.append(node.right)
            
            if rightSide:
                res.append(rightSide.val)
        
        return res
        