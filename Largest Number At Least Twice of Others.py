class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        copy_num = nums.copy()
        copy_num.remove(max_num)
        b = max(copy_num)
        if max_num >= (b * 2):
            return nums.index(max_num)
        else:
            return -1
