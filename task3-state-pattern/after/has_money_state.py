from vending_state import VendingState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vending_machine import VendingMachine


class HasMoneyState(VendingState):
    def insert_coin(self, machine: 'VendingMachine', amount: float) -> None:
        machine.balance += amount
        print(f'Added {amount}. Balance: {machine.balance}')

    def select_product(self, machine: 'VendingMachine', product_id: str) -> None:
        product = machine.products.get(product_id)
        if not product:
            print('Invalid product')
            return

        if product['stock'] == 0:
            from out_of_stock_state import OutOfStockState
            machine.set_state(OutOfStockState())
            return

        if machine.balance < product['price']:
            print(f'Insufficient funds. Need {product["price"]}')
            return

        from dispensing_state import DispensingState
        machine.set_state(DispensingState())
        machine.balance -= product['price']
        product['stock'] -= 1
        print(f'Dispensing {product["name"]}')

        if product['stock'] == 0:
            from out_of_stock_state import OutOfStockState
            machine.set_state(OutOfStockState())
        else:
            from idle_state import IdleState
            machine.set_state(IdleState())

    def cancel(self, machine: 'VendingMachine') -> None:
        print(f'Returning {machine.balance}')
        machine.balance = 0
        from idle_state import IdleState
        machine.set_state(IdleState())

    def refill(self, machine: 'VendingMachine', product_id: str, quantity: int) -> None:
        print('Cannot refill, transaction in progress')
