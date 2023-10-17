class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            row = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
            triangle.append(row)
        return triangle
