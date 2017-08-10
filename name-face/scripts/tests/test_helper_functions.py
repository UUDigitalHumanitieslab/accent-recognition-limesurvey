import pytest
from ..helper_functions import *


white_lines_test_cases = [
    {
        "str": "\n",
        "expected": ""
    },
    {
        "str": "    \n",
        "expected": ""
    },
    {
        "str": " \n     ",
        "expected": ""
    },
    {
        "str": "    \n text \n",
        "expected": " text \n"
    },
    {
        "str": "\n      \n     \n",
        "expected": ""
    },
    {
        "str": "this is a string",
        "expected": "this is a string"
    },
]


@pytest.fixture(scope="module", params=white_lines_test_cases)
def white_lines_test_case(request):
    return request.param

def test_remove_white_lines(white_lines_test_case):
    result = remove_white_lines(white_lines_test_case["str"])
    assert white_lines_test_case["expected"] == result


trailing_white_spaces_test_cases = [
    {
        "str": "\n",
        "expected": "\n"
    },
    {
        "str": "    \n",
        "expected": "    \n"
    },
    {
        "str": " \n     ",
        "expected": " \n"
    },
    {
        "str": "    \n text \n",
        "expected": "    \n text \n"
    },
    {
        "str": "\n      \n     \n",
        "expected": "\n      \n     \n",
    },
    {
        "str": "this is a string",
        "expected": "this is a string"
    },
    {
        "str": "",
        "expected": ""
    },
    {
        "str": " ",
        "expected": ""
    }
]

@pytest.fixture(scope="module", params=trailing_white_spaces_test_cases)
def trailing_white_spaces_test_case(request):
    return request.param

def test_remove_trailing_white_spaces(trailing_white_spaces_test_case):
    result = remove_trailing_white_spaces(trailing_white_spaces_test_case["str"])
    assert trailing_white_spaces_test_case["expected"] == result
