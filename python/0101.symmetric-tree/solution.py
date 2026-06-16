# Created by 林玮 (Jade Lin) at 2026/06/16 23:15
# leetgo: 1.4.15
# https://leetcode.cn/problems/symmetric-tree/

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.iterate(root, arr)
        for row in arr[1:]:
            size = len(row) // 2
            if row[:size] != row[size:][::-1]:
                return False

        return True

    def iterate(self, root: Optional[TreeNode], arr: List[int], depth=0):
        if depth >= len(arr):
            arr.append([])

        if root is None:
            arr[depth].append(None)
            return

        self.iterate(root.right, arr, depth + 1)
        arr[depth].append(root.val)
        self.iterate(root.left, arr, depth + 1)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSymmetric(root)
    print("\noutput:", serialize(ans, "boolean"))
