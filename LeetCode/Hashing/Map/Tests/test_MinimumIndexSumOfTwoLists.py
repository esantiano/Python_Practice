import pytest

from Hashing.Map.MinimumIndexSumOfTwoLists import Solution

def test_find_restaurant_normal():
    list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    assert Solution().findRestaurant(list1, list2) == ["Shogun"]

def test_find_restaurant_edge_tie():
    list1=["A", "B", "C"]
    list2=["C", "B", "A"]
    assert Solution().findRestaurant(list1, list2) == ["A", "B", "C"]

def test_find_restaurant_edge_tie_same_order():
    list1=["A", "B", "C"]
    list2=["A", "B", "C"]
    assert Solution().findRestaurant(list1, list2) == ["A"]

def test_find_restaurant_edge__end():
    list1=["X", "Y", "Z", "Common"]
    list2=["P", "Q", "Common"]
    assert Solution().findRestaurant(list1, list2) == ["Common"]

def test_find_restaurant_edge_single():
    list1=["Only"]
    list2=["Only"]
    assert Solution().findRestaurant(list1, list2) == ["Only"]

def test_find_restaurant_edge_no_overlap():
    list1=["A"]
    list2=["B"]
    assert Solution().findRestaurant(list1, list2) == []

def test_find_restaurant_edge_one_empty():
    list1=[]
    list2=["B"]
    assert Solution().findRestaurant(list1, list2) == []

def test_find_restaurant_edge_both_empty():
    list1=[]
    list2=[]
    assert Solution().findRestaurant(list1, list2) == []

def test_find_restaurant_edge_not_first_match():
    list1=["KFC", "Burger King", "Taco Bell", "Shogun"]
    list2=["Shogun", "KFC", "Burger King"]
    assert Solution().findRestaurant(list1, list2) == ["KFC"]



# ---------------------------findRestaurant2--------------------------

def test_find_restaurant2_normal():
    list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    assert Solution().findRestaurant2(list1, list2) == ["Shogun"]

def test_find_restaurant2_edge_tie():
    list1=["A", "B", "C"]
    list2=["C", "B", "A"]
    assert Solution().findRestaurant2(list1, list2) == ["A", "B", "C"] or Solution().findRestaurant2(list1, list2) == ["C", "B", "A"]

def test_find_restaurant2_edge_tie_same_order():
    list1=["A", "B", "C"]
    list2=["A", "B", "C"]
    assert Solution().findRestaurant2(list1, list2) == ["A"]

def test_find_restaurant2_edge__end():
    list1=["X", "Y", "Z", "Common"]
    list2=["P", "Q", "Common"]
    assert Solution().findRestaurant2(list1, list2) == ["Common"]

def test_find_restaurant2_edge_single():
    list1=["Only"]
    list2=["Only"]
    assert Solution().findRestaurant2(list1, list2) == ["Only"]

def test_find_restaurant2_edge_no_overlap():
    list1=["A"]
    list2=["B"]
    assert Solution().findRestaurant2(list1, list2) == []

def test_find_restaurant2_edge_one_empty():
    list1=[]
    list2=["B"]
    assert Solution().findRestaurant2(list1, list2) == []

def test_find_restaurant2_edge_both_empty():
    list1=[]
    list2=[]
    assert Solution().findRestaurant2(list1, list2) == []

def test_find_restaurant2_edge_not_first_match():
    list1=["KFC", "Burger King", "Taco Bell", "Shogun"]
    list2=["Shogun", "KFC", "Burger King"]
    assert Solution().findRestaurant2(list1, list2) == ["KFC"]