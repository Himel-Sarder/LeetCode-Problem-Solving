class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        babu = []
        sona = []
        for love in nums:
            if love not in sona:
                sona.append(love)
            else:
                babu.append(love)
        for love in range(1,len(nums)+1):
            if love not in nums:
                babu.append(love)
        return babu
