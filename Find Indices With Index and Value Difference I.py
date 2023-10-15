class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        result = [-1, -1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [int(i), int(j)]
        return result
