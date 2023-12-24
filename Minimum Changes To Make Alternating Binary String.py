class Solution:
    def minOperations(self, s: str) -> int:
        # Initialize counters for scenarios starting with '0' and '1'
        count_0 = 0
        count_1 = 0

        # Iterate through the string
        for i in range(len(s)):
            # Expected character for '0' and '1' at the current position
            expected_char_0 = str(i % 2)
            expected_char_1 = str(1 - i % 2)

            # Count operations for starting with '0'
            if s[i] == expected_char_0:
                count_0 += 1

            # Count operations for starting with '1'
            if s[i] == expected_char_1:
                count_1 += 1

        # Return the minimum count of operations
        return min(count_0, count_1)
