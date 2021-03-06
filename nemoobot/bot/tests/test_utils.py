import pytest
import requests
from unittest.mock import MagicMock
from mock import patch
from pytest_mock import mocker

from bot.utils import load_user_settings


@pytest.fixture
def setup_mock_get_method(mocker):
    mocker.patch('requests.get')
    yield requests.get


def test_load_user_settings_returns_list_if_any_error(setup_mock_get_method):
    mock_requests = setup_mock_get_method.return_value
    mock_requests.json.return_value.raise_exception.side_effect = KeyError()

    result = load_user_settings()
    assert list() == result
