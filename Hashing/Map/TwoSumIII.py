# Design a data structure for two sum
# Time: O(n) - for find since we need to go through every number in the map
#       O(1) - for adding
# Space: O(n) - we will store numbers in a map
# Algorithm for find: we get the complement value and first check to see if the number and complement are equal, if they are then we need to ensure that there are two copies of the number in the table
class TwoSum:
    # use map
    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number]+=1
        else:
            self.nums[number]=1

    def find(self, value: int) -> bool:
        for number in self.nums.keys():
            complement = value-number
            if number!=complement:
                if complement in self.nums:
                    return True
            elif self.nums[complement]>1: #In a particular case, where the number and its complement are equal, we then need to check if there exists at least two copies of the number in the table.
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)