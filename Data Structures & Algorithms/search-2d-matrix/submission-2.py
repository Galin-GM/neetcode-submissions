class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        i = -1

        while l <= r:

            mid = l + (r - l) // 2
            print(mid)
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                i = mid
                break
        
        if i == -1:
            return False

        l, r = 0, len(matrix[i])

        while l <= r:
            mid = l + (r - l) // 2

            if target == matrix[i][mid]:
                return True
            elif target > matrix[i][mid]:
                l = mid + 1
            else:
                r = mid - 1

        return False