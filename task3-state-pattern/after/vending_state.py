from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vending_machine import VendingMachine


class VendingState(ABC):
    @abstractmethod
    def insert_coin(self, machine: 'VendingMachine', amount: float) -> None:
        pass

    @abstractmethod
    def select_product(self, machine: 'VendingMachine', product_id: str) -> None:
        pass

    @abstractmethod
    def cancel(self, machine: 'VendingMachine') -> None:
        pass

    @abstractmethod
    def refill(self, machine: 'VendingMachine', product_id: str, quantity: int) -> None:
        pass
