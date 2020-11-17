def test_method():
    first = input()
    assert first.isdigit() == True
    second = input()
    assert second.isdigit() == True
    third = input()
    assert third.isdigit() == True
    assert (first + second < third or first + third < second or second + third < first) == False
