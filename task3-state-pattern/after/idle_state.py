from vending_state import VendingState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vending_machine import VendingMachine


class IdleState(VendingState):
    def insert_coin(self, machine: 'VendingMachine', amount: float) -> None:
        machine.balance += amount
        print(f'Accepted {amount}. Balance: {machine.balance}')
        from has_money_state import HasMoneyState
        machine.set_state(HasMoneyState())

    def select_product(self, machine: 'VendingMachine', product_id: str) -> None:
        print('Please insert money first')

    def cancel(self, machine: 'VendingMachine') -> None:
        print('No transaction to cancel')

    def refill(self, machine: 'VendingMachine', product_id: str, quantity: int) -> None:
        if product_id in machine.products:
            machine.products[product_id]['stock'] += quantity
            print(f'Refilled {product_id} with {quantity} units')
