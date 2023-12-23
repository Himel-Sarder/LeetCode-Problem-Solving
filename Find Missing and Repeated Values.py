class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = [element for sublist in grid for element in sublist]
        arr.sort()
        n = []

        # Find the repeated value
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                repeated_value = arr[i]
                break

        # Find the missing value
        arr_set = set(arr)
        for i in range(1, len(arr) + 2):
            if i not in arr_set:
                missing_value = i
                break

        return [repeated_value, missing_value]
