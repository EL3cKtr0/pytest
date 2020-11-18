import logging

filename = 'log.txt'

# create logger
logger = logging.getLogger('LogExample')
logger.setLevel(logging.DEBUG)

# create file
file = logging.FileHandler(filename)
file.setLevel(logging.DEBUG)
logger.addHandler(file)

def istriangle(l1, l2, l3):
    if l1 + l2 < l3:
        logger.error("ERROR, third number is bigger than the sum other two")
        return True
    if l1 + l3 < l2:
        logger.error("ERROR, second number is bigger than the sum other two")
        return True
    if l2 + l3 < l1:
        logger.error("ERROR, first number is bigger than the sum other two")
        return True

    return False


def test_method():
    first = input()
    if not first.isdigit():
        logger.error('ERROR, it must be a digit!')
    assert first.isdigit() == True
    second = input()
    if not second.isdigit():
        logger.error('ERROR, it must be a digit!')
    assert second.isdigit() == True
    third = input()
    if not third.isdigit():
        logger.error('ERROR, it must be a digit!')
    assert third.isdigit() == True

    logger.debug("All 3 numbers are valid for testing")

    assert istriangle(first, second, third) == False
