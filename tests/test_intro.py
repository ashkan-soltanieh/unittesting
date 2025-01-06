from src.intro import find_max, get_coupons


def test_find_max_should_return_the_first_argument_if_it_is_greater():
    # Arrange
    a = 2
    b = 1

    # Act
    result = find_max(a, b)

    # Assert
    assert result == a


def test_find_max_should_return_the_second_argument_if_it_is_greater():
    assert find_max(1, 2) == 2


def test_find_max_should_return_the_first_argument_if_arguments_are_equal():
    assert find_max(1, 1) == 1


def test_get_coupons_returns_array_with_items():
    assert len(get_coupons()) > 0


def test_get_coupons_contain_code_and_discount_as_keys():
    assert "code" in get_coupons()[0].keys()
    assert "discount" in get_coupons()[0].keys()


def test_get_coupons_code_is_string_type():
    assert isinstance(get_coupons()[0]["code"], str)


def test_get_coupons_discount_is_float_type():
    assert isinstance(get_coupons()[0]["discount"], float)
