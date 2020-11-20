import logging

filename = 'log.txt'

# create logger
logger = logging.getLogger('LogExample')
logger.setLevel(logging.DEBUG)


def istriangle(l1, l2, l3):
    if isinstance(l1, str) or isinstance(l2, str) or isinstance(l3, str):
        return False

    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return False

    if (l1 + l2) <= l3 or (l1 + l3) <= l2 or (l2 + l3) <= l1:
        return False

    return True


def test_method():
    assert istriangle(3, 4, 7) == False  # Should return False, this is NOT a Triangle
    assert istriangle(5, 5, 5) == True  # Should return True, this is a Triangle
    assert istriangle(0, 0, 0) == False  # Should return False, can't be a Triangle
    assert istriangle('ciao', 4, 7) == False  # Should return False, passing a string
    assert istriangle(-2, 1, 1) == False  # Should return False, one side is negative
    assert istriangle(2, 1, -1) == False  # Should return False, one side is negative
    assert istriangle(-5, -5, -5) == False  # Should return False, all 3 numbers are negative
