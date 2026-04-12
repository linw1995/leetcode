# Created by 林玮 (Jade Lin) at 2026/04/12 16:01
# leetgo: 1.4.15
# https://leetcode.cn/problems/two-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
