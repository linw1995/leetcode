# Created by 林玮 (Jade Lin) at 2026/02/06 16:10
# leetgo: 1.4.15
# https://leetcode.cn/problems/is-unique-lcci/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isUnique(self, astr: str) -> bool:
        size = len(astr)
        for i in range(size - 1):
            for j in range(i+1, size):
                if astr[i] == astr[j]:
                    return False
        return True
        

# @lc code=end

if __name__ == "__main__":
    astr: str = deserialize("str", read_line())
    ans = Solution().isUnique(astr)
    print("\noutput:", serialize(ans, "boolean"))
