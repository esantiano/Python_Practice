# Time: O(n*k) = O(nsqrt(n)) where k is the number of perfect squares 
# SpaceL O(n) - space for the queue and visited set
# algorithm: 
# the total number of numbers we have to check is n 
# the worst case is the solution is n where we use 1 
# use a list of the perfect squares to use from 1 to n
# we need to keep track of nodes or remainder we've seen 
# we also want to use a queue with tuple (remainder, step) 
# we grab the first tuple from the queue should be the current value and how many steps we are at currently
# then we iterate through the list of squares first subtract the square from the current value 
# compare the difference 
# if its 0 then we return an incremented step since we used one more square  
# if its less than 0 then there's no need to iterate through the rest of the squares list
# if the difference isnt inside the visited set then we'll want to add it to visited and add it as a tuple along with an incremented step
import collections
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        visited = set([n])
        q = collections.deque()
        q.append((n,0))        
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i+=1
        
        while q:
            remainder,step = q.popleft()
            for square in squares:
                diff = remainder - square
                if diff == 0:
                    return step + 1
                if diff < 0:
                    break
                if diff not in visited:
                    visited.add(diff)
                    q.append((diff,step+1))
                    
        return n