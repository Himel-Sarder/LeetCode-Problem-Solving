class Solution:
    def minimumSum(self, nums: List[int]) -> int:
         return min((sum(x) for x in combinations(nums, 3) if x[0] < x[1] > x[2]), default=-1)
