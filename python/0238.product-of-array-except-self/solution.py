# Created by 林玮 (Jade Lin) at 2026/03/16 10:17
# leetgo: 1.4.15
# https://leetcode.cn/problems/product-of-array-except-self/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L, R = [1], [1]
        for idx, num in enumerate(nums[:-1]):
            L.append(L[idx] * num)

        for idx, num in enumerate(reversed(nums[1:])):
            R.append(R[idx] * num)

        R.reverse()

        return [l * r for (l, r) in zip(L, R)]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().productExceptSelf(nums)
    print("\noutput:", serialize(ans, "integer[]"))
