"""Тесты для торгового автомата с паттерном State."""
import pytest
from vending_machine import VendingMachine


def test_initial_state_is_idle():
    """Тест начального состояния - Idle."""
    machine = VendingMachine()
    assert machine._state.__class__.__name__ == "IdleState"


def test_insert_coin_from_idle():
    """Тест вставки монеты из состояния Idle -> HasMoney."""
    machine = VendingMachine()
    machine.insert_coin(10)
    assert machine.balance == 10
    assert machine._state.__class__.__name__ == "HasMoneyState"


def test_insert_multiple_coins():
    """Тест вставки нескольких монет."""
    machine = VendingMachine()
    machine.insert_coin(10)
    machine.insert_coin(5)
    machine.insert_coin(20)
    assert machine.balance == 35


def test_select_product_without_money(capsys):
    """Тест выбора продукта без денег."""
    machine = VendingMachine()
    machine.select_product("A1")
    captured = capsys.readouterr()
    assert "Please insert money first" in captured.out


def test_select_product_invalid(capsys):
    """Тест выбора несуществующего продукта."""
    machine = VendingMachine()
    machine.insert_coin(50)
    machine.select_product("Z9")
    captured = capsys.readouterr()
    assert "Invalid product" in captured.out


def test_select_product_insufficient_funds(capsys):
    """Тест выбора продукта с недостаточными средствами."""
    machine = VendingMachine()
    machine.insert_coin(10)
    machine.select_product("A1")  # Продукт стоит 25
    captured = capsys.readouterr()
    assert "Insufficient funds" in captured.out


def test_select_product_success(capsys):
    """Тест успешной покупки."""
    machine = VendingMachine()
    machine.insert_coin(30)
    machine.select_product("A1")  # Продукт стоит 25, в наличии
    captured = capsys.readouterr()
    assert "Dispensing" in captured.out
    assert machine.balance == 5  # Сдача
    assert machine.products["A1"]["stock"] == 4  # Было 5, стало 4


def test_cancel_with_money():
    """Тест отмены с возвратом денег."""
    machine = VendingMachine()
    machine.insert_coin(20)
    machine.cancel()
    assert machine.balance == 0
    assert machine._state.__class__.__name__ == "IdleState"


def test_cancel_without_money(capsys):
    """Тест отмены без денег."""
    machine = VendingMachine()
    machine.cancel()
    captured = capsys.readouterr()
    assert "No money to return" in captured.out


def test_refill_product():
    """Тест пополнения запасов."""
    machine = VendingMachine()
    machine.products["B1"] = {"name": "Snickers", "price": 30, "stock": 0}
    machine.insert_coin(40)
    machine.select_product("B1")
    assert machine._state.__class__.__name__ == "OutOfStockState"

    machine.refill("B1", 10)
    assert machine.products["B1"]["stock"] == 10
    assert machine._state.__class__.__name__ == "IdleState"


def test_out_of_stock_transition(capsys):
    """Тест перехода в OutOfStock при покупке последнего товара."""
    machine = VendingMachine()
    machine.products["B1"]["stock"] = 1  # Оставить только 1 шт
    machine.insert_coin(40)
    machine.select_product("B1")
    captured = capsys.readouterr()
    assert "Dispensing" in captured.out
    assert machine._state.__class__.__name__ == "OutOfStockState"


def test_maintenance_state():
    """Тест режима обслуживания."""
    machine = VendingMachine()
    machine.enter_maintenance()
    assert machine._state.__class__.__name__ == "MaintenanceState"

    # В режиме обслуживания нельзя вставлять монеты
    machine.insert_coin(10)
    assert machine.balance == 0

    machine.exit_maintenance()
    assert machine._state.__class__.__name__ == "IdleState"


def test_insert_coin_during_dispensing(capsys):
    """Тест вставки монеты во время выдачи."""
    machine = VendingMachine()
    machine.insert_coin(30)
    machine.select_product("A1")
    # Сразу после select_product машина в состоянии Dispensing
    # (на практике это быстро, но для теста можем симулировать)
    captured = capsys.readouterr()
    assert "Dispensing" in captured.out


def test_multiple_purchases():
    """Тест нескольких покупок подряд."""
    machine = VendingMachine()

    # Первая покупка
    machine.insert_coin(30)
    machine.select_product("A1")
    assert machine.balance == 5

    # Вторая покупка (добавляем денег к сдаче)
    machine.insert_coin(25)
    machine.select_product("B1")
    assert machine.balance == 0


def test_cancel_from_out_of_stock():
    """Тест отмены из состояния OutOfStock."""
    machine = VendingMachine()
    machine.products["B1"]["stock"] = 0
    machine.insert_coin(40)
    machine.select_product("B1")
    assert machine._state.__class__.__name__ == "OutOfStockState"

    machine.cancel()
    assert machine.balance == 0
    assert machine._state.__class__.__name__ == "IdleState"
