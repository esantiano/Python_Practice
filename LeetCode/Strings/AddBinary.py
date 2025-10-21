# Given two binary strings a and b, return their sum as a binary string.
# Example 1:
#   Input: a = "11", b = "1"
#   Output: "100"
# adding two 1's together we get 0 with a carry over of 1 
# adding 1 to 0 we get 1 with no carry over
# adding two 0's together we get 0 with no carry over

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # we'll start at the end of each string
        i = len(a)-1
        j = len(b)-1

        carry = 0
        result = ""
        while i >= 0 or j >= 0: # we iterate backwards through each string
            if i >= 0: # we need to check the boundary of i in case it goes negative -> if it does then we will start looking at the end of the string
                if a[i] == "1":
                    carry += 1
            if j >= 0: # same boundary check needs to happen here 
                if b[j] == "1":
                    carry += 1
            
            if carry % 2 == 1: # handle the carry addition
                result = "1" + result # 0 + 1 = 1 
            else:
                result = "0" + result # 1 + 1 = 0 
            
            carry = carry//2 # take the leftover carry once we have determined which integer (1 or 0) to add 
            # the math looks like this: 
            # carry   11
            #          11 => 3
            #        + 11 => 3
            #        ----  
            #         110 => 6  
            # for the first column: 1 + 1 = 0 carry(1)
            # for the second column: carry(1) + (1 + 1) 0 = 1 carry(1)
            # for the third column: nothing(0) + carry(1) = 1
            # This line of code,
            # carry = carry // 2, determines the carry to the next position in the binary addition.
            # In binary arithmetic, when you add two bits (and a possible carry from the previous position), the sum can be 0, 1, 2, or 3:
            #     0 + 0 + 0 = 0 (binary 0)
            #     0 + 0 + 1 = 1 (binary 1)
            #     0 + 1 + 1 = 2 (binary 10)
            #     1 + 1 + 1 = 3 (binary 11) 

            # The rightmost digit of the binary sum becomes the current digit in the result, and the leftmost digit becomes the carry to the next position. 
            # The // 2 operation (integer division) correctly calculates this carry:
            #     If carry is 0 or 1, carry // 2 is 0, so the carry is 0.
            #     If carry is 2 or 3, carry // 2 is 1, so the carry is 1. 
            i-=1
            j-=1

        if carry == 1: # if we have an extra carry at the end then we just add 1 to the beginning of the result
            result = "1" + result
        return result

sol = Solution()
result = sol.addBinary("1010","1011")
print(result)