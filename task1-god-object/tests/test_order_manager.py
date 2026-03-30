import pytest
from unittest.mock import Mock, MagicMock
import sys
sys.path.insert(0, '../after')
from order_manager import OrderManager


def test_create_order_success():
    user_validator = Mock()
    user_validator.validate = Mock()
    user_validator.get_user_email = Mock(return_value='user@test.com')

    inventory_service = Mock()
    inventory_service.validate_availability = Mock()
    inventory_service.get_item_price = Mock(return_value=100.0)
    inventory_service.reserve_items = Mock()

    price_calculator = Mock()
    price_calculator.calculate_total = Mock(return_value=110.0)

    order_repository = Mock()
    order_repository.get_next_order_id = Mock(return_value=1)
    order_repository.save_order = Mock()

    notification_service = Mock()
    notification_service.send_notification = Mock()

    promo_code_resolver = Mock()
    discount_strategy = Mock()
    discount_strategy.calculate_discount = Mock(return_value=0.0)
    promo_code_resolver.get_discount_strategy = Mock(return_value=discount_strategy)

    manager = OrderManager(
        user_validator,
        inventory_service,
        price_calculator,
        order_repository,
        notification_service,
        promo_code_resolver
    )

    order = manager.create_order('user1', {'item1': 2})

    user_validator.validate.assert_called_once_with('user1')
    inventory_service.validate_availability.assert_called_once_with({'item1': 2})
    inventory_service.reserve_items.assert_called_once_with({'item1': 2})
    order_repository.save_order.assert_called_once()
    notification_service.send_notification.assert_called_once()

    assert order['id'] == 1
    assert order['user'] == 'user1'
    assert order['total'] == 110.0
    assert order['status'] == 'new'


def test_create_order_with_promo_code():
    user_validator = Mock()
    user_validator.validate = Mock()
    user_validator.get_user_email = Mock(return_value='user@test.com')

    inventory_service = Mock()
    inventory_service.validate_availability = Mock()
    inventory_service.get_item_price = Mock(return_value=100.0)
    inventory_service.reserve_items = Mock()

    price_calculator = Mock()
    price_calculator.calculate_total = Mock(return_value=99.0)

    order_repository = Mock()
    order_repository.get_next_order_id = Mock(return_value=1)
    order_repository.save_order = Mock()

    notification_service = Mock()
    notification_service.send_notification = Mock()

    promo_code_resolver = Mock()
    discount_strategy = Mock()
    discount_strategy.calculate_discount = Mock(return_value=0.1)
    promo_code_resolver.get_discount_strategy = Mock(return_value=discount_strategy)

    manager = OrderManager(
        user_validator,
        inventory_service,
        price_calculator,
        order_repository,
        notification_service,
        promo_code_resolver
    )

    order = manager.create_order('user1', {'item1': 2}, 'SAVE10')

    promo_code_resolver.get_discount_strategy.assert_called_once_with('SAVE10')
    assert order['total'] == 99.0
