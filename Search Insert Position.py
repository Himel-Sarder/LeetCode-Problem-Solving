class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)-1):
                if nums[i] < target < nums[i+1]:
                    return i+1
                elif target > nums[len(nums)-1]:
                    return len(nums)
            if len(nums) < 2:
                if target > nums[0]:
                    return 1
        return 0
