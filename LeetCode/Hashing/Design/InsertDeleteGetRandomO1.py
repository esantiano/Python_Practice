# Time O(1): The challenge was to get an average of O(1) time complexity for each of the operations in this class
# Space O(N): We use a map and list to store the values 
# Design:

# Storage: 
# use a list to keep track of elements in the randomized set
# use a dict to keep track of the indexes of values in the set

# Insert: 
# list append and checking/adding values to a dict is O(1) average time

# Remove 
# we need to do a swap here since list.remove(val) is an average of O(n) time, 
# to remove we need to replace the value given within the list with 
# the last element in the list then we can pop the last element from the list which is O(1) time
# we also need to remove the given value from the dictionary O(1) time
# this will effectively remove the given value

# getRandom 
# selecting a random index and then returning is O(1)

import random
class RandomizedSet:

    def __init__(self):
        self.randomList = [] 
        self.randomDict = {} 

    def insert(self, val: int) -> bool:
        if val in self.randomDict:
            return False
        self.randomList.append(val)
        self.randomDict[val]=len(self.randomList)-1
        return True

    def remove(self, val: int) -> bool: 
        if val in self.randomDict:
            lastEl, valIndex = self.randomList[-1], self.randomDict[val] # get the last element in the list and the index of the value to remove
            self.randomList[valIndex] = lastEl # place the last element of the list at the index of the value to be removed
            self.randomList.pop() # remove the duplicated last element
            self.randomDict[lastEl] = valIndex # update the index of the last element in the dictionary 
            del self.randomDict[val] # delete the given value from the dictionary 
            return True
        return False

    def getRandom(self) -> int:
        n = len(self.randomList)-1 # this can all be replaced using random.choice(self.randomList)
        rand = random.randint(0,n)
        return self.randomList[rand]

