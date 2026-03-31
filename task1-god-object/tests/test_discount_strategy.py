import pytest
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    FixedDiscount,
    PromoCodeResolver,
)


def test_no_discount():
    strategy = NoDiscount()
    assert strategy.calculate_discount(100.0) == 0.0


def test_percentage_discount():
    strategy = PercentageDiscount(0.1)
    assert strategy.calculate_discount(100.0) == 0.1


def test_percentage_discount_20():
    strategy = PercentageDiscount(0.2)
    assert strategy.calculate_discount(100.0) == 0.2


def test_fixed_discount():
    strategy = FixedDiscount(10.0)
    assert strategy.calculate_discount(100.0) == 0.1


def test_fixed_discount_exceeds_amount():
    strategy = FixedDiscount(150.0)
    assert strategy.calculate_discount(100.0) == 1.0


def test_promo_code_resolver_save10():
    resolver = PromoCodeResolver()
    strategy = resolver.get_discount_strategy("SAVE10")
    assert isinstance(strategy, PercentageDiscount)
    assert strategy.calculate_discount(100.0) == 0.1


def test_promo_code_resolver_save20():
    resolver = PromoCodeResolver()
    strategy = resolver.get_discount_strategy("SAVE20")
    assert isinstance(strategy, PercentageDiscount)
    assert strategy.calculate_discount(100.0) == 0.2


def test_promo_code_resolver_invalid_code():
    resolver = PromoCodeResolver()
    strategy = resolver.get_discount_strategy("INVALID")
    assert isinstance(strategy, NoDiscount)


def test_promo_code_resolver_no_code():
    resolver = PromoCodeResolver()
    strategy = resolver.get_discount_strategy()
    assert isinstance(strategy, NoDiscount)
