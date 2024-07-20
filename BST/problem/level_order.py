# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# leetcode 102: Binary Tree Level Order Traversal

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:



# result:
# ...........................................
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
        

# youtube:    https://www.youtube.com/watch?v=LkaIRwx0Hww&t=734s