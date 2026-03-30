from vending_state import VendingState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vending_machine import VendingMachine


class MaintenanceState(VendingState):
    def insert_coin(self, machine: 'VendingMachine', amount: float) -> None:
        print('Machine under maintenance. Returning coin.')

    def select_product(self, machine: 'VendingMachine', product_id: str) -> None:
        print('Machine under maintenance')

    def cancel(self, machine: 'VendingMachine') -> None:
        print('Machine under maintenance')

    def refill(self, machine: 'VendingMachine', product_id: str, quantity: int) -> None:
        if product_id in machine.products:
            machine.products[product_id]['stock'] += quantity
            print(f'Refilled {product_id} with {quantity} units during maintenance')
