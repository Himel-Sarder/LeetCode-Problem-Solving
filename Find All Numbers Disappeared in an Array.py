class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_numbers = set(range(1, n + 1))
        missing_numbers = list(all_numbers - set(nums))
        return missing_numbers
