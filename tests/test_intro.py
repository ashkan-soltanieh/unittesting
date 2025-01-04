from src.intro import find_max


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
