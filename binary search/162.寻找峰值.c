/*
 * @lc app=leetcode.cn id=162 lang=c
 *
 * [162] 寻找峰值
 *
 * https://leetcode-cn.com/problems/find-peak-element/description/
 *
 * algorithms
 * Medium (42.41%)
 * Likes:    167
 * Dislikes: 0
 * Total Accepted:    33.9K
 * Total Submissions: 74.7K
 * Testcase Example:  '[1,2,3,1]'
 *
 * 峰值元素是指其值大于左右相邻值的元素。
 *
 * 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
 *
 * 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
 *
 * 你可以假设 nums[-1] = nums[n] = -∞。
 *
 * 示例 1:
 *
 * 输入: nums = [1,2,3,1]
 * 输出: 2
 * 解释: 3 是峰值元素，你的函数应该返回其索引 2。
 *
 * 示例 2:
 *
 * 输入: nums = [1,2,1,3,5,6,4]
 * 输出: 1 或 5
 * 解释: 你的函数可以返回索引 1，其峰值元素为 2；
 * 或者返回索引 5， 其峰值元素为 6。
 *
 *
 * 说明:
 *
 * 你的解法应该是 O(logN) 时间复杂度的。
 *
 */

// @lc code=start
#define __WITH_LOG__

#ifdef __WITH_LOG__
#include <stdio.h>
#define LOG(message, args...)                                                  \
  fprintf(stdout, "| %s:%d | " message "\n", __FUNCTION__, __LINE__, ##args)
#else
#define LOG(message, args...)
#endif
int findPeakElement(int *nums, int numsSize) {
  // it possible that the peak on one of two sides.
  int low = 0, high = numsSize, mid = (low + high) / 2;
  while (low < high && low != mid) {
    LOG("low %d, mid %d, high %d", low, mid, high);
    if (nums[mid - 1] > nums[mid]) {
      LOG("descends");
      high = mid;
    } else {
      LOG("ascends");
      low = mid;
    }
    mid = (high + low) / 2;
  }
  return low;
}

// @lc code=end
