import pytest
import sys
sys.path.insert(0, '../after')
from inventory_service import InventoryService


def test_validate_availability_success():
    inventory = {
        'item1': {'price': 100.0, 'stock': 10},
        'item2': {'price': 50.0, 'stock': 5}
    }
    service = InventoryService(inventory)
    service.validate_availability({'item1': 5, 'item2': 3})


def test_validate_availability_item_not_found():
    inventory = {'item1': {'price': 100.0, 'stock': 10}}
    service = InventoryService(inventory)
    with pytest.raises(ValueError, match='Item item2 not found'):
        service.validate_availability({'item2': 1})


def test_validate_availability_insufficient_stock():
    inventory = {'item1': {'price': 100.0, 'stock': 5}}
    service = InventoryService(inventory)
    with pytest.raises(ValueError, match='Insufficient stock for item1'):
        service.validate_availability({'item1': 10})


def test_get_item_price():
    inventory = {'item1': {'price': 100.0, 'stock': 10}}
    service = InventoryService(inventory)
    assert service.get_item_price('item1') == 100.0


def test_reserve_items():
    inventory = {'item1': {'price': 100.0, 'stock': 10}}
    service = InventoryService(inventory)
    service.reserve_items({'item1': 3})
    assert inventory['item1']['stock'] == 7
