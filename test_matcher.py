import pytest 
from matcher import match 

def test_full_match(): 
     assert match("Python Java" , "python java") == 100.0 

def test_no_match():
     assert match("Python Java", "Ruby Go") == 0.0 

def test_partial_match():
     assert match("Python Java C++", "I Know python well") == pytest.approx(33.33, rel=0.01)

