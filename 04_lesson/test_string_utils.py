import pytest
from string_utils import StringUtils

utils = StringUtils()


# --- capitalize ---
def test_capitalize_normal():
    assert utils.capitalize("тест") == "Тест"


def test_capitalize_already_capital():
    assert utils.capitalize("Тест") == "Тест"


def test_capitalize_error():
    with pytest.raises(TypeError):
        utils.capitalize(123)


# --- upper ---
def test_upper_lowercase():
    assert utils.upper("abc") == "ABC"


def test_upper_mixed():
    assert utils.upper("aBcD") == "ABCD"


def test_upper_error():
    with pytest.raises(TypeError):
        utils.upper(None)


# --- join ---
def test_join_strings():
    assert utils.join(["a", "b", "c"], "-") == "a-b-c"


def test_join_empty_list():
    assert utils.join([], ",") == ""


def test_join_error():
    with pytest.raises(TypeError):
        utils.join(["a", 1], ",")


# --- split ---
def test_split_default():
    assert utils.split("a b c") == ["a", "b", "c"]


def test_split_custom():
    assert utils.split("a|b|c", "|") == ["a", "b", "c"]


def test_split_error():
    with pytest.raises(TypeError):
        utils.split(42)
