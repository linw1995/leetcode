/*
 * @lc app=leetcode.cn id=153 lang=c
 *
 * [153] 寻找旋转排序数组中的最小值
 *
 * https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
 *
 * algorithms
 * Medium (49.70%)
 * Likes:    158
 * Dislikes: 0
 * Total Accepted:    38.8K
 * Total Submissions: 77.3K
 * Testcase Example:  '[3,4,5,1,2]'
 *
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 *
 * ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
 *
 * 请找出其中最小的元素。
 *
 * 你可以假设数组中不存在重复元素。
 *
 * 示例 1:
 *
 * 输入: [3,4,5,1,2]
 * 输出: 1
 *
 * 示例 2:
 *
 * 输入: [4,5,6,7,0,1,2]
 * 输出: 0
 *
 */

// @lc code=start

int findMin(int *nums, int numsSize) {
  if (nums[0] < nums[numsSize - 1] || numsSize - 1 == 0) {
    return nums[0];
  }
  int mid = numsSize / 2;
  int left = findMin(nums, mid);
  int right = findMin(nums + mid, numsSize - mid);
  return left < right ? left : right;
}

// @lc code=end
