# Задание 1: God Object - OrderManager

## Анализ проблем

### Code Smells

#### 1. God Object / Large Class
Класс `OrderManager` отвечает за слишком много несвязанных функций:
- Валидация пользователей (строки 14-17)
- Управление инвентарем (строки 18-22, 30-31)
- Расчет цен и применение скидок (строки 23-28)
- Работа с базой данных (строка 35)
- Отправка email-уведомлений (строки 36-40)

#### 2. Long Method
Метод `create_order()` содержит 28 строк кода и выполняет множество разных операций.

#### 3. Shotgun Surgery
Для добавления нового типа скидки нужно изменять условия в методе (строки 27-28).

#### 4. Tight Coupling
- Прямое использование `smtplib` внутри метода
- Зависимость от конкретной реализации базы данных

#### 5. Security Issues
- SQL Injection (строка 35): `self.db.execute(f'INSERT INTO orders VALUES ({order})')`
- Hardcoded email (строка 39)

### Нарушения принципов SOLID

#### 1. SRP (Single Responsibility Principle) - НАРУШЕН
Класс имеет 5 различных ответственностей: валидация, инвентарь, расчет цен, БД, уведомления.

#### 2. OCP (Open/Closed Principle) - НАРУШЕН
Строки 27-28:
```python
if promo_code == 'SAVE10': total *= 0.9
elif promo_code == 'SAVE20': total *= 0.8
```
Для добавления нового промокода нужно изменять код метода.

#### 3. DIP (Dependency Inversion Principle) - НАРУШЕН
Класс зависит от конкретных реализаций (прямое создание `smtplib.SMTP`, прямой вызов `db.execute`), а не от абстракций.

### Метрики

#### Цикломатическая сложность метода `create_order()`

Подсчет условных переходов:
- Базовая сложность: 1
- `if user_id not in self.users`: +1
- `if self.users[user_id]['banned']`: +1
- `for item_id, qty in items.items()`: +1
- `if item_id not in self.inventory`: +1
- `if self.inventory[item_id]['stock'] < qty`: +1
- `for item_id, qty in items.items()`: +1
- `if promo_code == 'SAVE10'`: +1
- `elif promo_code == 'SAVE20'`: +1
- `for item_id, qty in items.items()`: +1

**Цикломатическая сложность ДО: 10** (норма <= 5)

## Решение

### Выделенные классы

1. **UserValidator** - валидация пользователей и получение их данных
2. **InventoryService** - управление запасами товаров
3. **PriceCalculator** - расчет итоговой стоимости с учетом налогов
4. **OrderRepository** - сохранение заказов в базу данных
5. **NotificationService** - отправка уведомлений (абстракция + EmailNotificationService)
6. **DiscountStrategy** - паттерн Strategy для скидок (NoDiscount, PercentageDiscount, FixedDiscount)
7. **PromoCodeResolver** - преобразование промокода в стратегию скидки

### Применение паттерна Strategy

Паттерн Strategy использован для скидок:
- Интерфейс `DiscountStrategy` с методом `calculate_discount()`
- Конкретные реализации: `NoDiscount`, `PercentageDiscount`, `FixedDiscount`
- `PromoCodeResolver` для преобразования промокода в стратегию

Теперь добавление нового типа скидки не требует изменения существующего кода (OCP).

### Как решены проблемы SOLID

- **SRP**: Каждый класс имеет одну ответственность
- **OCP**: Новые типы скидок добавляются через новые классы стратегий
- **DIP**: OrderManager зависит от абстракций (NotificationService, DiscountStrategy)

## UML-диаграммы

### Диаграмма классов ДО рефакторинга

```mermaid
classDiagram
    class OrderManager {
        -db
        -smtp_host
        -smtp_port
        -tax_rate
        -currency
        -orders
        -users
        -inventory
        +create_order(user_id, items, promo_code)
    }
```

### Диаграмма классов ПОСЛЕ рефакторинга

```mermaid
classDiagram
    class OrderManager {
        -user_validator
        -inventory_service
        -price_calculator
        -order_repository
        -notification_service
        -promo_code_resolver
        +create_order(user_id, items, promo_code)
    }

    class UserValidator {
        -users
        +validate(user_id)
        +get_user_email(user_id)
    }

    class InventoryService {
        -inventory
        +validate_availability(items)
        +get_item_price(item_id)
        +reserve_items(items)
    }

    class PriceCalculator {
        -tax_rate
        +calculate_total(items, item_prices, discount)
    }

    class OrderRepository {
        -db
        -orders
        +save_order(order)
        +get_next_order_id()
    }

    class NotificationService {
        <<abstract>>
        +send_notification(recipient, subject, message)
    }

    class EmailNotificationService {
        -smtp_host
        -smtp_port
        -sender_email
        +send_notification(recipient, subject, message)
    }

    class DiscountStrategy {
        <<abstract>>
        +calculate_discount(amount)
    }

    class NoDiscount {
        +calculate_discount(amount)
    }

    class PercentageDiscount {
        -percentage
        +calculate_discount(amount)
    }

    class FixedDiscount {
        -fixed_amount
        +calculate_discount(amount)
    }

    class PromoCodeResolver {
        -promo_codes
        +get_discount_strategy(promo_code)
    }

    OrderManager --> UserValidator
    OrderManager --> InventoryService
    OrderManager --> PriceCalculator
    OrderManager --> OrderRepository
    OrderManager --> NotificationService
    OrderManager --> PromoCodeResolver

    NotificationService <|-- EmailNotificationService
    DiscountStrategy <|-- NoDiscount
    DiscountStrategy <|-- PercentageDiscount
    DiscountStrategy <|-- FixedDiscount
    PromoCodeResolver --> DiscountStrategy
```

## Метрики

### Сравнение метрик ДО и ПОСЛЕ

| Метрика | ДО | ПОСЛЕ |
|---------|-----|-------|
| Цикломатическая сложность create_order() | 10 | 2 |
| Количество классов | 1 | 7 |
| Количество ответственностей | 5 | 1 (на класс) |
| Связанность (coupling) | Высокая | Низкая |
| Тестируемость | Низкая | Высокая |

### Цикломатическая сложность ПОСЛЕ



Метод `create_order()` в новой версии:
- Базовая сложность: 1
- Последовательные вызовы без ветвлений: +1

**Цикломатическая сложность ПОСЛЕ: 2** (отличный результат)

## Как запустить тесты

```bash
cd task1-god-object
pytest tests/
```
