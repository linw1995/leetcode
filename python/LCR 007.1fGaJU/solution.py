# Created by 林玮 (Jade Lin) at 2026/02/13 16:32
# leetgo: 1.4.15
# https://leetcode.cn/problems/1fGaJU/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        ans = dict()
        for j in range(1, size - 1):
            i = 0
            k = size - 1
            while i < j and j < k:
                target = (nums[i], nums[j], nums[k])
                s = sum(target)
                if s == 0:
                    key = frozenset(target)
                    ans[key] = target
                    i += 1
                elif s < 0:
                    i += 1
                else:
                    k -= 1

        return list(map(list, ans.values()))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeSum(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
