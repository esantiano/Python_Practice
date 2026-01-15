import pytest
from Hashing.Design.UniqueWordAbbreviation import ValidWordAbbr, ValidWordAbbr2

def test():
    sol = ValidWordAbbr(["deer","door","cake","card"])
    assert sol.isUnique("dear") == False
    assert sol.isUnique("door") == False
    assert sol.isUnique("cart") == True
    assert sol.isUnique("cake") == True