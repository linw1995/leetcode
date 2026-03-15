# Created by 林玮 (Jade Lin) at 2026/03/15 20:12
# leetgo: 1.4.15
# https://leetcode.cn/problems/shuffle-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = nums[:]
        ans[0::2] = nums[:n]
        ans[1::2] = nums[n:]
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().shuffle(nums, n)
    print("\noutput:", serialize(ans, "integer[]"))
