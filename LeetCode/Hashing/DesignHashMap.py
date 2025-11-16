# Time: O(N/K) - N number of all possible values , k - value of key (number of predefined buckets)
# worst case average bucket size is N/K
# worst case is we have to scan a bucket O(N/K)
# Space O(K+M) M - number of unique values that have been inserted into the hash set 
# Design in this approach we are using 2 arrays
# the first class Bucket uses an array datasctructure that stores kvp sets 
# the second class MyHashMap uses the array datastructure and uses a key to determine which bucket we place kvps into

class Bucket():
    def __init__(self):
        self.bucket = []

    def get(self,key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self,key,value):
        found = False
        for i,kv in enumerate(self.bucket): # get the index of the bucket where we could find the kvp 
            if kv[0] == key: # we update if the key exists
                self.bucket[i] = (key,value) 
                found = True
                break
        if not found: # we insert if key does not exist
            self.bucket.append((key,value))

    def remove(self,key):
        for i,(k,v) in enumerate(self.bucket): # get the index of the bucket where we could find the kvp 
            if key == k:
                del self.bucket[i]

class MyHashMap:

    def __init__(self):
        self.key_range = 2069
        self.buckets = [Bucket() for i in range(self.key_range)]
    
    def put(self, key: int, value: int) -> None:
        self.buckets[key%self.key_range].update(key,value)

    def get(self, key: int) -> int:
        return self.buckets[key%self.key_range].get(key)

    def remove(self, key: int) -> None:
        self.buckets[key%self.key_range].remove(key)

def test_put_and_get_single():
    m = MyHashMap()
    m.put(1, 10)
    assert m.get(1) == 10
    assert m.get(2) == -1  # key not present


def test_overwrite_value():
    m = MyHashMap()
    m.put(1, 10)
    m.put(1, 20)  # overwrite existing key
    assert m.get(1) == 20


def test_multiple_keys_independent():
    m = MyHashMap()
    m.put(1, 10)
    m.put(2, 20)
    m.put(3, 30)

    assert m.get(1) == 10
    assert m.get(2) == 20
    assert m.get(3) == 30


def test_remove_existing_key():
    m = MyHashMap()
    m.put(1, 10)
    m.put(2, 20)

    m.remove(1)
    assert m.get(1) == -1   # removed
    assert m.get(2) == 20   # other key unaffected


def test_remove_nonexistent_key():
    m = MyHashMap()
    m.put(1, 10)

    m.remove(2)             # removing key that doesn't exist
    assert m.get(1) == 10   # should still be there
    assert m.get(2) == -1


def test_delete_head_node_in_internal_list():
    """
    This ensures deleting the first real node after dummy head works.
    """
    m = MyHashMap()
    m.put(1, 10)
    m.put(2, 20)  # in your list, this will be right after head

    m.remove(2)   # depending on insertion order, adjust if needed
    # With your current implementation, new nodes go at head.next,
    # so insertion order is: head -> 2 -> 1
    # So deleting key=2 deletes the first node after dummy.

    assert m.get(2) == -1
    assert m.get(1) == 10


def test_delete_middle_does_not_break_list():
    """
    This test is designed to catch the 'prev never moves' bug in delete().
    With your current delete implementation, this will FAIL.
    After you fix delete by updating prev inside the loop, it should pass.
    """
    m = MyHashMap()
    # Remember: Map.add inserts new nodes at the front:
    # After these puts, internal list is: head -> 3 -> 2 -> 1
    m.put(1, 10)
    m.put(2, 20)
    m.put(3, 30)

    # Remove the middle node in the internal list (key=2)
    m.remove(2)

    # Expected behavior:
    #  - key 2 removed
    #  - keys 1 and 3 still present
    assert m.get(2) == -1, "Key 2 should have been removed"
    assert m.get(3) == 30, "Key 3 should still exist"
    assert m.get(1) == 10, "Key 1 should still exist"


def test_update_existing_after_many_inserts():
    m = MyHashMap()
    for i in range(10):
        m.put(i, i * 10)

    # update some of them
    m.put(3, 999)
    m.put(7, 777)

    assert m.get(3) == 999
    assert m.get(7) == 777
    assert m.get(0) == 0
    assert m.get(9) == 90


if __name__ == "__main__":
    # Run all tests
    test_put_and_get_single()
    test_overwrite_value()
    test_multiple_keys_independent()
    test_remove_existing_key()
    test_remove_nonexistent_key()
    test_delete_head_node_in_internal_list()
    test_delete_middle_does_not_break_list()
    test_update_existing_after_many_inserts()

    print("All tests passed (except any that exposed known bugs).")
