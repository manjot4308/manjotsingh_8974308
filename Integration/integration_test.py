from sorting import sort_five_numbers

# Positive test case (should pass)
def test_sort_five_numbers_positive():
    sorted_nums = sort_five_numbers(5, 3, 9, 1, 7)
    assert sorted_nums == [1, 3, 5, 7, 9], "Sorting failed for positive case"

# Negative test case (should fail)
def test_sort_five_numbers_negative():
    sorted_nums = sort_five_numbers(5, 3, 9, 1, 7)
    assert sorted_nums == [5, 3, 9, 1, 7], "Sorting failed for negative case"

