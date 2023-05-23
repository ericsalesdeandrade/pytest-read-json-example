import pathlib
import pytest
from read_json.core import compute_birth_year


def test_compute_birth_year_1():
    input_data = '{"name": "John", "age": 30, "city": "New York"}'
    expected = "John was born in 1993"
    assert compute_birth_year(input_data) == expected


def test_compute_birth_year_2():
    file = pathlib.Path("tests/unit/test_data/input1.json")
    with open(file) as f:
        input_data = f.read()
    expected = "Jerry was born in 1968"
    assert compute_birth_year(input_data) == expected


def test_compute_birth_year_3(input_json):
    expected = "Eric was born in 1991"
    assert compute_birth_year(input_json) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ('{"name": "Robin", "age": 55, "city": "Los Angeles"}', "Robin was born in 1968"),
    ])
def test_compute_birth_year_4(input_data, expected):
    assert compute_birth_year(input_data) == expected


def test_compute_birth_year_5(input_json_command_line):
    expected = "Ravi was born in 1933"
    assert compute_birth_year(input_json_command_line) == expected
