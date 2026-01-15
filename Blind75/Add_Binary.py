class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2) # we can use int() to convert binary strings to integers, we need the raw string to be in binary and use a base 2
        y = int(b,2)
        while y: 
            answer = x^y # XOR operation gives us the sum without carrying
            carry = (x&y) << 1 # AND operation gives us the carry, we need to shift it left by 1 to add it to the correct position
            # we repeat the process until there is no carry left
            x,y = answer, carry 
            
        return bin(x)[2:]