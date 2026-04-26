# Created by 林玮 (Jade Lin) at 2026/04/26 13:29
# leetgo: 1.4.15
# https://leetcode.cn/problems/binary-tree-level-order-traversal/

from typing import *
from leetgo_py import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=begin


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(root: Optional[TreeNode], depth: int = 0):
            if root is None:
                return

            if depth == len(ans):
                ans.append([])

            ans[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
