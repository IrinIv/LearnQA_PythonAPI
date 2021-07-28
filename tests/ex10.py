import pytest

def test_phrase():
    phrase = input("Set a phrase: ")
    expected_result = (int(len(phrase)))
    print(int(len(phrase)))


    assert expected_result < 15, "The phrase is greater than 15 characters"


