from typing import Dict, Any

class InventoryService:
    def __init__(self, inventory: Dict[str, Dict[str, Any]]):
        self.inventory = inventory

    def validate_availability(self, items: Dict[str, int]) -> None:
        for item_id, qty in items.items():
            if item_id not in self.inventory:
                raise ValueError(f'Item {item_id} not found')

            if self.inventory[item_id]['stock'] < qty:
                raise ValueError(f'Insufficient stock for {item_id}')

    def get_item_price(self, item_id: str) -> float:
        return self.inventory[item_id]['price']

    def reserve_items(self, items: Dict[str, int]) -> None:
        for item_id, qty in items.items():
            self.inventory[item_id]['stock'] -= qty
