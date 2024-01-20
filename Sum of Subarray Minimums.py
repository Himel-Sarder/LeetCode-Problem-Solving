class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0

        # Iterate through the array, maintaining a stack of indices
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                # Calculate the contribution of the popped element to the result
                popped_index = stack.pop()
                result += arr[popped_index] * (i - popped_index) * (popped_index - (stack[-1] if stack else -1))
                result %= MOD

            stack.append(i)

        # Process remaining elements in the stack
        while stack:
            popped_index = stack.pop()
            result += arr[popped_index] * (len(arr) - popped_index) * (popped_index - (stack[-1] if stack else -1))
            result %= MOD

        return result
