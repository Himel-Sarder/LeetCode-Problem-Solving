class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        total = 0
        for a in ascii_lowercase:
          i, j = s.find(a), s.rfind(a)
          if i < j:
            total += len(set(s[i+1:j]))
        return total
