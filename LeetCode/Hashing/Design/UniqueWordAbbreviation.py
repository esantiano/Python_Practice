
# Time: For abbreviate: O(K) - k is longest word we go through each character in a word to create the abbreviation
#       For fill abr dict: O(N) - we abbreviate each word and then place inside the dictionary list 
#       For isUnique: O(1) - we abbreviate the word and then check the dictionary list
# Space O(n) - we use two data structures, a list and dictionary 

# Design: We store the given dictionary in a list, we design a hashmap for the abbreviations and matching words abbr:list relationship
# we use a function to abbreviate each word and another to fill the hashmap
# isUnique checks for the existence of an abbreviation in the hashmap as well as the length of the list and the existence of the word in the list

# Requirements
# boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
#     There is no word in dictionary whose abbreviation is equal to word's abbreviation.
#     For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.
#       ** for any dictionary if there are two words that have been given that have the same abbreviation they are automatically considered not unique.

from typing import List
from collections import defaultdict
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dict = dictionary
        self.abbr_dict = defaultdict(list)
        self.fillAbbrDict()
        
    def abbreviate(self,word):
        if len(word)<=2:
            return word
        start=word[0]
        end=word[-1]
        count=0
        for _ in word:
            count+=1
        return start+str(count-2)+end
    
    def fillAbbrDict(self):
        for word in self.dict:
            abbr = self.abbreviate(word)
            if word not in self.abbr_dict[abbr]:
                self.abbr_dict[abbr].append(word)

    def isUnique(self, word: str) -> bool:
        abbr = self.abbreviate(word)
        collection = self.abbr_dict.get(abbr)
        return collection is None or (len(collection)==1 and word in collection)


# Design: Another way we can design this is to use a hashmap to get a count of the abbreviations from the list and a set to store all the unique words in the given list. 
# isUnique would only have to check the hashmap for existence and count while the set could be used to check the existence of the word in the given dictionary 
class ValidWordAbbr2:

    def __init__(self, dictionary: List[str]):
        self.dict = set(dictionary)
        self.abbr_dict = defaultdict(int)
        self.fillAbbrDict()
        
    def abbreviate(self,word):
        if len(word)<=2:
            return word
        start=word[0]
        end=word[-1]
        count=0
        for _ in word:
            count+=1
        return start+str(count-2)+end
    
    def fillAbbrDict(self):
        for word in self.dict:
            abbr = self.abbreviate(word)
            self.abbr_dict[abbr]+=1

    def isUnique(self, word: str) -> bool:
        abbr = self.abbreviate(word)
        count = self.abbr_dict.get(abbr)
        return count==0 or (count==1 and word in self.dict) 
    