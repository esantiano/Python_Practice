# time o(nlogm) n length of nums m - max number in nums
# space o(1)
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            # this operation can be replaced with count = int(math.floor(math.log10(num)))+1
            count = 1
            while num>=10:
                num/=10
                count+=1
            if count%2 == 0:
                result+=1 
        return result
    
# time O(n) - since we pass through once and just compare numbers in num according to constraints
# space O(1)
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        # Counter to count the number of even digit integers
        even_digit_count = 0

        for num in nums:
            if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999)\
            or num == 100000:
                even_digit_count += 1

        return even_digit_count
