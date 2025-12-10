# Time O(n + L) - where n = len(s), L = len(result), we parse over s and produce an output, creating each result cur_str*k takes L time
# Space O(L) - where L is the len(result) - the stack holds the resulting string


# Algorithm: 
# there are two cases 
# nested k[stringk[string]] # decode the inner pattern first 
# regular k[string]
# we process s left to right and use a stack to hold all the characters we've seen so far
# we'll push everything but ] onto the stack 
# when we see ] we've reached the end of an encoded block k[...]
# we will" 
# pop characters from the stack to get the inner sub string
# when removing characters from the stack we will get the inner sub string in reversed order, we will have to reverse the popped characters to get the correct substring
# pop digits from the stack to get k 
# k will also be popped in reverse order from the substring ( if k has more than one digit), so we'll have to reverse k as well 
# push the resulting inner * k back onto the stack 
#
# return the joined stack 
class SolutionSingleStack:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                cur = []
                while stack and stack[-1] != '[': # collect substring inside [...]
                    cur.append(stack.pop())
                stack.pop()  # remove '['
                substring = ''.join(reversed(cur)) # reverse the substring

                num = []
                while stack and stack[-1].isdigit(): # collect number before [
                    num.append(stack.pop())
                num.reverse() # reverse the number

                k = int(''.join(num)) if num else 1
                stack.append(substring * k) # place the resulting substring back onto the stack
        return ''.join(stack)


# Time O(n + L) - where n = len(s), L = len(result), we parse over s and produce an output, creating each result cur_str*k takes L time
# Space O(L + d) or O(n + d) - L = len(result), d = maximum nesting depth [[[]]] etc.... n - each stack needs to hold one item per [, L - each result must be created and added to the current string

# Algorithm
# use a stack here to store strings
# use a stack to store numbers
# use a list to store the current string
# use a variable to store the current number
# use an index to iterate through s 
# iterate through s 
# read the current index 
# encounter a digit build the current number 
# encounter a [ then add the current number and current string into their respective stacks and reset both variables
# encounter a ] decode
# when we decode:
# we take the top number on the number stack
# take the top string on the string stack
# get the result of the current string * k 
# set the current string equal to the list of the string from the top of string stack and result of current string * k 
# increment the index
# return the joined current string
class SolutionDoubleStack:
    def decodeString(self, s: str) -> str:
        strStack = []
        diStack = []
        cur_str = []
        cur_num = 0
        index = 0
        
        while index < len(s):
            c = s[index]
            if c.isdigit():
                cur_num = cur_num*10 + int(c)
            elif c == "[":
                diStack.append(cur_num)
                strStack.append("".join(cur_str))
                cur_num = 0
                cur_str = []
            elif c.isalpha():
                cur_str.append(c)
            elif c == "]":
                k = diStack.pop()
                prev_str = strStack.pop()
                result = "".join(cur_str)*k
                cur_str = [prev_str + result]
            index += 1
        return "".join(cur_str)

# Time O(n+L) - where n = len(s), L = len(result), we parse over s and produce an output decodedString, add decodedString*k into a list and return the joined list
# Space O(L+d) L = len(result), each time we see k[...] we recurse, d = max nesting depth of brackets, here if we have multiple brackets nested inside eachother we have d calls on the call stack, each DFS call builds a result list then joins it into a string

# Algorithm: 
# here we are using index as a shared nonlocal pointer
# the DFS() function decodes everything starting at index until it goes out of bounds or reaches ]
# we use a result list to store alphabetical characters in s 
# within the iteration we are looking for two conditions:
# if current character is an alphabetical character then we add it to the result list and move the index
# if the current character is a digit then we determine what k is, since k could be more than one digit we need to move the index until we reach a non digit character
# once we determine k we skip over the "[" (increment the index)
# then we recurse and assign the result to a variable decodedString
# afterwards we skip over "]" (increment the index) this is done in order to process the rest of s
# then we append the result of k*decodedString to the result list
# finally we return the joined result list
class SolutionRecursion:
    def decodeString(self, s: str) -> str:
        index = 0

        def DFS():
            nonlocal index
            result = []
            
            while index < len(s) and s[index] != "]": # make sure index is in bounds and we dont hit "]" while we iterate through s, this is acting as our null check
                if s[index].isalpha(): # build result 
                    result.append(s[index])
                    index+=1
                elif s[index].isdigit(): # build k
                    k = 0 
                    while index < len(s) and s[index].isdigit():
                        k = k*10 + int(s[index])
                        index+=1
                    index+=1 # skip over "["
                    decodedString = DFS() # recursive call
                    index+=1 # skip over "]"
                    result.append(decodedString * k)

            return "".join(result)

        return DFS()