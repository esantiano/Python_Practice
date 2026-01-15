# Time: O(N/K) - N number of all possible values , k - value of key (number of predefined buckets)
# worst case average bucket size is N/K
# worst case is we have to scan a bucket O(N/K)
# Space O(K+M) M - number of unique values that have been inserted into the hash set 
# Design in this approach we are using an array to store bucket indexes and linked lists as the buckets (stores the values we want to insert/remove/search)
class MyHashSet:

    def __init__(self):
        self.keyRange = 769 # create a key for the set
        self.buckets = [Bucket() for i in range(self.keyRange)] # create buckets to store values 
    
    def _hash(self,val):
        return val%self.keyRange

    def add(self, key: int) -> None:
        # get the bucket we need to add to
        bucket_index = self._hash(key)
        # call the bucket add function
        self.buckets[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.buckets[bucket_index].delete(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return self.buckets[bucket_index].exists(key)

class Node:
    def __init__(self,x,nextNode=None):
        self.val = x
        self.next = nextNode
        
class Bucket: # implementation of a linked list
    def __init__(self):
        self.head = Node(0)
    
    def insert(self,val):
        if not self.exists(val):
            newNode = Node(val, self.head.next)
            self.head.next = newNode

    def delete(self,val):
        cur = self.head.next
        prev = self.head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                return 
            prev = cur
            cur = cur.next

    def exists(self,val):
        cur = self.head.next
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

def run_tests():
    # Helper to create a fresh set for each test
    def make_set():
        return MyHashSet()

    # 1. Basic add + contains
    s = make_set()
    s.add(1)
    s.add(2)
    assert s.contains(1) is True, "1 should be in the set"
    assert s.contains(2) is True, "2 should be in the set"
    assert s.contains(3) is False, "3 should not be in the set"

    # 2. Duplicate adds should not break anything
    s = make_set()
    s.add(5)
    s.add(5)
    s.add(5)
    assert s.contains(5) is True, "5 should still be in the set after duplicate adds"
    s.remove(5)
    assert s.contains(5) is False, "5 should be removed even after many adds"

    # 3. Remove existing elements
    s = make_set()
    s.add(10)
    s.add(20)
    assert s.contains(10) is True
    assert s.contains(20) is True

    s.remove(10)
    assert s.contains(10) is False, "10 should be removed"
    assert s.contains(20) is True, "20 should still be present"

    # 4. Remove non-existent elements (should not crash or affect others)
    s = make_set()
    s.add(7)
    s.add(8)
    s.remove(9)  # 9 was never added
    assert s.contains(7) is True, "7 should still be present after removing non-existent 9"
    assert s.contains(8) is True, "8 should still be present after removing non-existent 9"

    # 5. Collision behavior: values that land in the same bucket
    s = make_set()
    base = 1
    collide = base + s.keyRange  # same bucket as `base` because of modulo
    s.add(base)
    s.add(collide)

    assert s.contains(base) is True, f"{base} should be in the set"
    assert s.contains(collide) is True, f"{collide} should be in the set"

    s.remove(base)
    assert s.contains(base) is False, f"{base} should be removed"
    assert s.contains(collide) is True, f"{collide} should still be in the set"

    # 6. Edge case: removing from an empty set
    s = make_set()
    s.remove(100)  # should not raise
    assert s.contains(100) is False, "100 should not be in an empty set"

    # 7. Mixed operations sequence (similar to LeetCode style)
    s = make_set()
    s.add(1)
    s.add(2)
    assert s.contains(1) is True
    assert s.contains(3) is False
    s.add(2)
    assert s.contains(2) is True
    s.remove(2)
    assert s.contains(2) is False

    print("✅ All tests passed!")


if __name__ == "__main__":
    run_tests()
