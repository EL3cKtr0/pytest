import pytest

def number(x):
    return x + 5

def test_method():
    assert number(4) == 8