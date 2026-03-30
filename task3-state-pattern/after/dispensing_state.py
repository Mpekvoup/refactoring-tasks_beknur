from vending_state import VendingState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vending_machine import VendingMachine


class DispensingState(VendingState):
    def insert_coin(self, machine: 'VendingMachine', amount: float) -> None:
        print('Please wait, dispensing...')

    def select_product(self, machine: 'VendingMachine', product_id: str) -> None:
        print('Please wait, dispensing...')

    def cancel(self, machine: 'VendingMachine') -> None:
        print('Cannot cancel, dispensing in progress')

    def refill(self, machine: 'VendingMachine', product_id: str, quantity: int) -> None:
        print('Cannot refill, dispensing in progress')
