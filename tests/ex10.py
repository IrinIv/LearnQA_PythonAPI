def test_phrase():
    phrase = input("Set a phrase: ")
    actual_result = (int(len(phrase)))
    print(int(len(phrase)))

    assert actual_result < 15, "The phrase is greater than 15 characters"
