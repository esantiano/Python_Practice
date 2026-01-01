# Time O(n+m) - where n is the length of the list rooms and m is the number of keys within each room.
# Space: O(n) - we use a list and stack to store rooms to visit and the status of rooms that we have already visited. 

# Notes: This problem has elements of a DFS algorithm, the lists within the list structure is similar to graph nodes, and determining whether or not it is possible to explore each node within the graph.

# Algorithm:
# we'll start with a list of Falses of size n to denote the room and their visited status
# we can also use a stack to hold the rooms that we need to visit 
# since room 0 is unlocked we place that room within the stack
# iterate through the list of rooms 
# for each room we'll check the keys to the other rooms 
# if we have keys to other rooms we add those rooms to the stack 
# once we access the room on the stack we'll change the room visited status 
# we'll determine if we are able to go through all the rooms based on the list
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        
        to_visit = [0]
        
        while to_visit:
            room = to_visit.pop()
            if not visited[room]:
                visited[room] = True
                for room in rooms[room]:
                    to_visit.append(room)
        return all(visited)
            