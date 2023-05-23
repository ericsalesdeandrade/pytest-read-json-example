import json

import pytest


@pytest.fixture(scope="session")
def input_json():
    return json.dumps({"name": "Eric", "age": 32, "city": "London"})


def pytest_addoption(parser):
    parser.addoption(
        "--input-json", action="store", default='{"name":"Rick", "age": 50, "city": "NY"}', help="Input JSON"
    )


@pytest.fixture
def input_json_command_line(request):
    return request.config.getoption("--input-json")
