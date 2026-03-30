from typing import Dict


class PriceCalculator:
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate

    def calculate_total(self, items: Dict[str, int], item_prices: Dict[str, float], discount: float = 0.0) -> float:
        subtotal = sum(item_prices[item_id] * qty for item_id, qty in items.items())
        discounted = subtotal * (1 - discount)
        total = discounted * (1 + self.tax_rate)
        return total
