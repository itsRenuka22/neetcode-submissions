# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #will have to first traverse the tree in inorder manner so that all nodes will be stored in ascending values
        st = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            node = st.pop()
            k -= 1
            if k == 0:
                return node.val
            curr = node.right
        
        