"""Тесты для торгового автомата с паттерном State."""
import pytest
from vending_machine import VendingMachine


@pytest.fixture
def products():
    """Фикстура с продуктами для автомата."""
    return {
        "A1": {"name": "Coke", "price": 25, "stock": 5},
        "B1": {"name": "Snickers", "price": 30, "stock": 3},
        "C1": {"name": "Water", "price": 15, "stock": 10}
    }


def test_initial_state_is_idle(products):
    """Тест начального состояния - Idle."""
    machine = VendingMachine(products)
    assert machine.state.__class__.__name__ == "IdleState"


def test_insert_coin_from_idle(products):
    """Тест вставки монеты из состояния Idle -> HasMoney."""
    machine = VendingMachine(products)
    machine.insert_coin(10)
    assert machine.balance == 10
    assert machine.state.__class__.__name__ == "HasMoneyState"


def test_insert_multiple_coins(products):
    """Тест вставки нескольких монет."""
    machine = VendingMachine(products)
    machine.insert_coin(10)
    machine.insert_coin(5)
    machine.insert_coin(20)
    assert machine.balance == 35


def test_select_product_without_money(products, capsys):
    """Тест выбора продукта без денег."""
    machine = VendingMachine(products)
    machine.select_product("A1")
    captured = capsys.readouterr()
    assert "Please insert money first" in captured.out


def test_select_product_invalid(products, capsys):
    """Тест выбора несуществующего продукта."""
    machine = VendingMachine(products)
    machine.insert_coin(50)
    machine.select_product("Z9")
    captured = capsys.readouterr()
    assert "Invalid product" in captured.out


def test_select_product_insufficient_funds(products, capsys):
    """Тест выбора продукта с недостаточными средствами."""
    machine = VendingMachine(products)
    machine.insert_coin(10)
    machine.select_product("A1")  # Продукт стоит 25
    captured = capsys.readouterr()
    assert "Insufficient funds" in captured.out


def test_select_product_success(products, capsys):
    """Тест успешной покупки."""
    machine = VendingMachine(products)
    machine.insert_coin(30)
    machine.select_product("A1")  # Продукт стоит 25, в наличии
    captured = capsys.readouterr()
    assert "Dispensing" in captured.out
    assert machine.balance == 5  # Сдача
    assert machine.products["A1"]["stock"] == 4  # Было 5, стало 4


def test_cancel_with_money(products):
    """Тест отмены с возвратом денег."""
    machine = VendingMachine(products)
    machine.insert_coin(20)
    machine.cancel()
    assert machine.balance == 0
    assert machine.state.__class__.__name__ == "IdleState"


def test_cancel_without_money(products, capsys):
    """Тест отмены без денег."""
    machine = VendingMachine(products)
    machine.cancel()
    captured = capsys.readouterr()
    assert "No transaction to cancel" in captured.out


def test_refill_product(products):
    """Тест пополнения запасов."""
    machine = VendingMachine(products)
    machine.products["B1"]["stock"] = 0
    machine.insert_coin(40)
    machine.select_product("B1")
    assert machine.state.__class__.__name__ == "OutOfStockState"

    machine.refill("B1", 10)
    assert machine.products["B1"]["stock"] == 10
    assert machine.state.__class__.__name__ == "IdleState"


def test_out_of_stock_transition(products, capsys):
    """Тест перехода в OutOfStock при покупке последнего товара."""
    machine = VendingMachine(products)
    machine.products["B1"]["stock"] = 1  # Оставить только 1 шт
    machine.insert_coin(40)
    machine.select_product("B1")
    captured = capsys.readouterr()
    assert "Dispensing" in captured.out
    assert machine.state.__class__.__name__ == "OutOfStockState"


def test_maintenance_state(products):
    """Тест режима обслуживания."""
    machine = VendingMachine(products)
    machine.enter_maintenance()
    assert machine.state.__class__.__name__ == "MaintenanceState"

    # В режиме обслуживания нельзя вставлять монеты
    machine.insert_coin(10)
    assert machine.balance == 0

    machine.exit_maintenance()
    assert machine.state.__class__.__name__ == "IdleState"


def test_insert_coin_during_dispensing(products, capsys):
    """Тест вставки монеты во время выдачи."""
    machine = VendingMachine(products)
    machine.insert_coin(30)
    machine.select_product("A1")
    captured = capsys.readouterr()
    assert "Dispensing" in captured.out


def test_multiple_purchases(products):
    """Тест нескольких покупок подряд."""
    machine = VendingMachine(products)

    # Первая покупка
    machine.insert_coin(30)
    machine.select_product("A1")
    assert machine.balance == 5

    # Вторая покупка (добавляем денег к сдаче)
    machine.insert_coin(25)
    machine.select_product("B1")
    assert machine.balance == 0


def test_cancel_from_out_of_stock(products):
    """Тест отмены из состояния OutOfStock."""
    machine = VendingMachine(products)
    machine.products["B1"]["stock"] = 0
    machine.insert_coin(40)
    machine.select_product("B1")
    assert machine.state.__class__.__name__ == "OutOfStockState"

    machine.cancel()
    assert machine.balance == 0
    assert machine.state.__class__.__name__ == "IdleState"
