# Created by 林玮 (Jade Lin) at 2026/03/11 17:40
# leetgo: 1.4.15
# https://leetcode.cn/problems/sort-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(begin, end):
            if end - begin <= 1:
                return

            mid = (end + begin) // 2
            merge_sort(begin, mid)
            merge_sort(mid, end)
            tmp = []
            i = begin
            j = mid
            while True:
                if i >= mid:
                    tmp.extend(nums[j:end])
                    break

                if j >= end:
                    tmp.extend(nums[i:mid])
                    break

                if nums[i] < nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1

            nums[begin:end] = tmp

        merge_sort(0, len(nums))
        return nums


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))
