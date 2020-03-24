/*
 * @lc app=leetcode.cn id=74 lang=c
 *
 * [74] 搜索二维矩阵
 *
 * https://leetcode-cn.com/problems/search-a-2d-matrix/description/
 *
 * algorithms
 * Medium (35.91%)
 * Likes:    148
 * Dislikes: 0
 * Total Accepted:    36.3K
 * Total Submissions: 96.4K
 * Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
 *
 * 编写一个高效的算法来判断 m x
 * n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
 *
 *
 * 每行中的整数从左到右按升序排列。
 * 每行的第一个整数大于前一行的最后一个整数。
 *
 *
 * 示例 1:
 *
 * 输入:
 * matrix = [
 * ⁠ [1,   3,  5,  7],
 * ⁠ [10, 11, 16, 20],
 * ⁠ [23, 30, 34, 50]
 * ]
 * target = 3
 * 输出: true
 *
 *
 * 示例 2:
 *
 * 输入:
 * matrix = [
 * ⁠ [1,   3,  5,  7],
 * ⁠ [10, 11, 16, 20],
 * ⁠ [23, 30, 34, 50]
 * ]
 * target = 13
 * 输出: false
 *
 */

// @lc code=start
#include <stdbool.h>

bool searchMatrix(int **matrix, int matrixSize, int *matrixColSize,
                  int target) {
  int rowSize = matrixSize;
  if (rowSize <= 0)
    return false;
  int colSize = matrixColSize[0];
  if (colSize <= 0)
    return false;

  int low = 0, high = rowSize * colSize, mid = (low + high) / 2;
  while (low < high) {
    int value = matrix[mid / colSize][mid % colSize];
    if (value < target) {
      low = mid + 1;
    } else if (value > target) {
      high = mid;
    } else {
      return true;
    }
    mid = (low + high) / 2;
  }
  return false;
}

// @lc code=end
