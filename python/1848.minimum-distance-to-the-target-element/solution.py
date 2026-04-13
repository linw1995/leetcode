# Created by 林玮 (Jade Lin) at 2026/04/13 12:47
# leetgo: 1.4.15
# https://leetcode.cn/problems/minimum-distance-to-the-target-element/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        i, j = start, start + 1

        while i >= 0 or j < n:
            if i >= 0:
                if nums[i] == target:
                    return abs(i - start)

                i -= 1

            if j < n:
                if nums[j] == target:
                    return abs(j - start)

                j += 1

        return start


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().getMinDistance(nums, target, start)
    print("\noutput:", serialize(ans, "integer"))
