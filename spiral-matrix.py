# 1  2  3  4
# 5  6  7  8
# 9 10 11 12
# 13 14 15 16
# [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        res = []

        while(top <= bottom and left <= right):
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            if top > bottom:
                break
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            if top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))