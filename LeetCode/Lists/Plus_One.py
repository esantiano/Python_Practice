# "Plus One" is a subset of the problem set "Add Number", which shares the same solution pattern.
# All these problems could be solved in linear time, and the question here is how to solve it without using the addition operation or how to solve it in constant space complexity.

# Integers
# Usually, the addition operation is not allowed for such a case. Use the Bit Manipulation Approach.


# Strings
# Use bit-by-bit computation. Note, sometimes it might not be feasible to come up with a solution with the constant space for languages with immutable strings, e.g. for Java and Python. Here is an example: Add Binary.

# Linked Lists
# Sentinel Head + Schoolbook Addition with Carry.

# Lists 
# Schoolbook addition with carry.
# Note that a straightforward idea to convert everything into integers and then apply the addition could be risky,

# Approach Schoolbook Addition with Carry Optimal
# Start from the end of the array and move backward 
# set all 9's at the end of the array to 0 
# for digits != 9 we increase by 1, we can return digits from here 
# if we exit the loop and all digits were 9 then we need to add 1 to the beginning of the list and return that

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        for i in range(n-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0 
            else:
                digits[i] += 1
                return digits
        return [1] + digits

sol = Solution()
res = sol.plusOne([9,9,0])
print(res)