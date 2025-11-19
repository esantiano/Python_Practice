# Time O(l1 + l2) - we need to run through each list at least once 
# Space O(l1*x) -  hashmap size grows upto l1*x where x refers to average string length.
# Algorithm:
# use a hashmap to create relationships for strings in list1 and indexes 
# use another hashmap to create relationships for strings in list2 and indexes 
# use an output list to store the output
# keep track of least index sum using variable
# determine the longer list/hashmap:
# loop through the shorter hashmap, look for the keys in the longer hashmap
# sum the indexes and add the string key sum pair to another hashmap
# compare the sum to the least index sum variable and update the least index sum
# iterate through the string sum hashmap 
# compare the sum to the least index sum
# add string keys with sums equal to least index sum to output list
# return the output list
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        string_map_1 = {}
        string_map_2 = {}
        
        for i,s in enumerate(list1):
            string_map_1[s] = i
        
        for i,s in enumerate(list2):
            string_map_2[s] = i
        
        short = None
        long = None
        if len(list1)<=len(list2):
            short = string_map_1
            long = string_map_2
        else:
            short = string_map_2
            long = string_map_1
        
        string_sum_map = {}
        least_index_sum = float("Inf")
        for key in short:
            if key not in long:
                continue 
            sum_indexes = short[key] + long.get(key,float("Inf"))
            string_sum_map[key] = sum_indexes 
            if sum_indexes < least_index_sum:
                least_index_sum = sum_indexes

        output = []
        for key in string_sum_map:
            index_sum = string_sum_map[key]
            if index_sum == least_index_sum:
                output.append(key)
        return output

# we can simplify this algorithm:
# use a hashmap for list1 store string:index
# initialize a variable for the least index sum to infinity
# initialize an output list
# iterate through list2 and check if any strings in list2 are in the hashmap
# if there are then sum the indexes and compare them to the least index sum
# clear the output list and add the string from list2 to the output if the sum is less thatn the least index sum
# if the sum is equal to the least index sum then add the string to output 
    def findRestaurant2(self, list1, list2):
        string_index_map = {string:i for i,string in enumerate(list1)}
        least_index_sum = float("Inf")
        output = []
        for j, s in enumerate(list2):
            if s in string_index_map:
                index_sum = string_index_map[s] + j
                if index_sum < least_index_sum:
                    output = [s] # clear the output list of old values and place the new string
                    least_index_sum = index_sum
                elif index_sum == least_index_sum:
                    output.append(s)
        return output