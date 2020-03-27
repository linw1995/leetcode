/*
 * @lc app=leetcode.cn id=81 lang=c
 *
 * [81] 搜索旋转排序数组 II
 *
 * https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/description/
 *
 * algorithms
 * Medium (34.16%)
 * Likes:    116
 * Dislikes: 0
 * Total Accepted:    21.5K
 * Total Submissions: 60.8K
 * Testcase Example:  '[2,5,6,0,0,1,2]\n0'
 *
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 *
 * ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
 *
 * 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
 *
 * 示例 1:
 *
 * 输入: nums = [2,5,6,0,0,1,2], target = 0
 * 输出: true
 *
 *
 * 示例 2:
 *
 * 输入: nums = [2,5,6,0,0,1,2], target = 3
 * 输出: false
 *
 * 进阶:
 *
 *
 * 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
 * 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
 *
 *
 */

// @lc code=start
#include <stdbool.h>
#define __WITH_LOG__

#ifdef __WITH_LOG__
#include <stdio.h>
#define LOG(message, args...)                                                  \
  fprintf(stdout, "| %s:%d | " message "\n", __FUNCTION__, __LINE__, ##args)
#else
#define LOG(message, args...)
#endif

bool search(int *nums, int numsSize, int target) {
  int low = 0, high = numsSize, mid = (high + low) / 2;
  while (low < high) {
    LOG("before cleaning the duplicated number from two sides. low %d, high "
        "%d, mid %d, val %d",
        low, high, mid, nums[mid]);
    while (low < high - 1 && nums[low] == nums[low + 1])
      low++;
    while (low < high - 1 && nums[high - 1] == nums[high - 2])
      high--;
    mid = (high + low) / 2;
    LOG("after cleaning the duplicated number from two sides. low %d, high "
        "%d, mid %d, val %d",
        low, high, mid, nums[mid]);
    int newLow = low, newHigh = high;
    if (nums[mid] < target) {
      newLow = mid + 1;
    } else if (nums[mid] > target) {
      newHigh = mid;
    } else {
      return true;
    }

    if (nums[low] > nums[mid]) {
      LOG("Left part is unsorted");
      int rv = search(nums + low, mid - low, target);
      if (rv == true)
        return true;
    }
    if (nums[mid] > nums[high - 1]) {
      LOG("Right part is unsorted");
      int rv = search(nums + mid, high - mid, target);
      if (rv == true)
        return true;
    }

    low = newLow;
    high = newHigh;
    mid = (low + high) / 2;
  }
  return false;
}
// @lc code=end
