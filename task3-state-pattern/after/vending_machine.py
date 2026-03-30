from typing import Dict, Any
from vending_state import VendingState
from idle_state import IdleState


class VendingMachine:
    def __init__(self, products: Dict[str, Dict[str, Any]]):
        self.products = products
        self.balance = 0.0
        self.state: VendingState = IdleState()

    def set_state(self, state: VendingState) -> None:
        self.state = state

    def insert_coin(self, amount: float) -> None:
        self.state.insert_coin(self, amount)

    def select_product(self, product_id: str) -> None:
        self.state.select_product(self, product_id)

    def cancel(self) -> None:
        self.state.cancel(self)

    def refill(self, product_id: str, quantity: int) -> None:
        self.state.refill(self, product_id, quantity)
