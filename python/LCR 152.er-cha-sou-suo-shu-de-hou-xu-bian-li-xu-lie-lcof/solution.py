# Created by 林玮 (Jade Lin) at 2026/03/13 11:05
# leetgo: 1.4.15
# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1:
            return True

        head = postorder[-1]
        for i, n in enumerate(postorder[:-1]):
            if n > head:
                left = postorder[:i]
                right = postorder[i:-1]
                for num in right:
                    if num < head:
                        return False

                return self.verifyTreeOrder(left) and self.verifyTreeOrder(right)

        return self.verifyTreeOrder(postorder[:-1])


# @lc code=end

if __name__ == "__main__":
    postorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().verifyTreeOrder(postorder)
    print("\noutput:", serialize(ans, "boolean"))
