from vending_state import VendingState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vending_machine import VendingMachine


class OutOfStockState(VendingState):
    def insert_coin(self, machine: 'VendingMachine', amount: float) -> None:
        print('Out of stock. Returning coin.')

    def select_product(self, machine: 'VendingMachine', product_id: str) -> None:
        print('Out of stock')

    def cancel(self, machine: 'VendingMachine') -> None:
        print(f'Returning {machine.balance}')
        machine.balance = 0
        from idle_state import IdleState
        machine.set_state(IdleState())

    def refill(self, machine: 'VendingMachine', product_id: str, quantity: int) -> None:
        if product_id in machine.products:
            machine.products[product_id]['stock'] += quantity
            print(f'Refilled {product_id} with {quantity} units')
            from idle_state import IdleState
            machine.set_state(IdleState())
