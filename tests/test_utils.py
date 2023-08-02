import io
import json

import pytest

from src import utils


@pytest.fixture
def parsed_json():
    with io.open('operations.json', encoding='utf-8') as file:
        return json.load(file)


def test_format_number_of_card():
    assert utils.format_number_of_card("Счет 38573816654581789611") == "Счет **9611"
    assert utils.format_number_of_card("МИР 8193813157568899") == "МИР 8193 81** **** 8899"
    assert utils.format_number_of_card("81938131") == ""


def test_get_5_last_operations():
    assert len(utils.get_5_last_operations()) == 5


def test_find_operation_by_id(parsed_json):
    assert type(utils.find_operation_by_id(parsed_json, 522357576)) is dict
