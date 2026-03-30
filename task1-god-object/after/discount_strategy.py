from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        return 0.0


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def calculate_discount(self, amount: float) -> float:
        return self.percentage


class FixedDiscount(DiscountStrategy):
    def __init__(self, fixed_amount: float):
        self.fixed_amount = fixed_amount

    def calculate_discount(self, amount: float) -> float:
        return min(self.fixed_amount / amount, 1.0) if amount > 0 else 0.0


class PromoCodeResolver:
    def __init__(self):
        self.promo_codes = {
            'SAVE10': PercentageDiscount(0.1),
            'SAVE20': PercentageDiscount(0.2),
        }

    def get_discount_strategy(self, promo_code: str = None) -> DiscountStrategy:
        if promo_code and promo_code in self.promo_codes:
            return self.promo_codes[promo_code]
        return NoDiscount()
