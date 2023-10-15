class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            num = 0
            
            for number in digits:
                num = num * 10 + number

            num += 1

            NewNums = [int(x) for x in str(num)]

            return NewNums
