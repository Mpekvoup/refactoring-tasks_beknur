from typing import Dict


class PriceCalculator:
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate

    def calculate_total(self, subtotal: float, discount: float = 0.0) -> float:
        discounted = subtotal * (1 - discount)
        total = discounted * (1 + self.tax_rate)
        return total
