import pytest
from unittest.mock import Mock
import sys
sys.path.insert(0, '../after')
from user_validator import UserValidator


def test_validate_existing_user():
    users = {'user1': {'email': 'test@test.com', 'banned': False}}
    validator = UserValidator(users)
    validator.validate('user1')


def test_validate_user_not_found():
    users = {}
    validator = UserValidator(users)
    with pytest.raises(ValueError, match='User user1 not found'):
        validator.validate('user1')


def test_validate_banned_user():
    users = {'user1': {'email': 'test@test.com', 'banned': True}}
    validator = UserValidator(users)
    with pytest.raises(ValueError, match='User user1 is banned'):
        validator.validate('user1')


def test_get_user_email():
    users = {'user1': {'email': 'test@test.com', 'banned': False}}
    validator = UserValidator(users)
    assert validator.get_user_email('user1') == 'test@test.com'
