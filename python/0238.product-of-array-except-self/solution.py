# Created by 林玮 (Jade Lin) at 2026/03/16 10:17
# leetgo: 1.4.15
# https://leetcode.cn/problems/product-of-array-except-self/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for idx, num in enumerate(nums[:-1]):
            ans.append(ans[idx] * num)

        size = len(nums)
        tmp = 1
        for idx, num in enumerate(reversed(nums[1:])):
            ans[size - idx - 1] *= tmp
            tmp = tmp * num

        ans[0] *= tmp

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().productExceptSelf(nums)
    print("\noutput:", serialize(ans, "integer[]"))
