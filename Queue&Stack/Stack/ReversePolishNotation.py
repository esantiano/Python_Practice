# Time O(N) - we iterate through the tokens list and process all the operators, we remove from the stack which is O(1)
# Space O(N) - we store the tokens within a stack
# we'll use a stack to store all the numbers 
# when we encounter an operator we will perform the operation on the top two numbers on the stack
# we need to take note of the order we do division, the first value on the stack should be the divisor (denominator) and the second the dividend(numerator)
# we need to take note of the order we do subtraction as well second on stack minus first on the stack
# then we'll push the result back onto the stack 
# we will continue this until we have iterated through the entire list 
# we can then return the final number within the stack
import operator
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        # this can be done using lambda functions, it might be better to use  lambda functions to understand how the numbers on the stack need to be popped for the division and subtraction operations
        operators = {"+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.truediv}
        for token in tokens:
            if token not in operators:
                nums.append(token)
            else:
                second,first = nums.pop(),nums.pop() # this is done with regard to the division and subtraction operators 
                result = int(operators[token](int(first), int(second)))
                nums.append(str(result))
        return int(nums[-1])