# Created by 林玮 (Jade Lin) at 2026/02/05 17:42
# leetgo: 1.4.15
# https://leetcode.cn/problems/transformed-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [self.transform(nums, i) for i in range(len(nums))]

    def transform(self, nums: List[int], i: int) -> int:
        offset = nums[i]
        i = i + offset
        if i < 0:
            i = (len(nums) - abs(i) % len(nums)) % len(nums)
        else:
            i = i % len(nums)

        if offset == 0:
            return 0
        else:
            return nums[i]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().constructTransformedArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))
