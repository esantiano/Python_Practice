# Time: O(logn) - the number of digits in a given number, the time used to calculate get_digit_total (we are processing each digit in the number, and the number of digits in a number is given by logn.)
# Space: O(logn) - we are using a set to store the digit_totals 
# Algorithm:
# calculate the digit total 
    # the digit total is calculated by squaring the remainder of n/10, n is divided by 10 until it reaches 0
# store the digit total in a variable
# if the digit total is equal to 1 return true
# if we have seen the digit total before return false
# add the digit total to the set
# recalculate the new digit total
class Solution:
    def get_digit_total(self, n: int) -> int:
        digit_total = 0
        while n>0: # use this to drive because we are reducing the given value
            digit_total += (n%10)**2
            n = n//10
        return digit_total
            
    def isHappy(self, n: int) -> bool:
        seen = set()
        iteration = self.get_digit_total(n)
        
        while True: # we can use the conditions in the if statements to drive
            if iteration == 1:
                return True
            if iteration in seen:
                return False
            seen.add(iteration)
            iteration = self.get_digit_total(iteration)

    def isHappy2(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen: # we use the reverse of the if condtions above to drive the loop
            seen.add(n)
            n = self.get_digit_total(n)
        return n == 1 