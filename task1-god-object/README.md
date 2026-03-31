# Задание 1: God Object - OrderManager

## Проблемы

Класс OrderManager делает слишком много всего - в нем и проверка пользователей, и работа с товарами, и база данных, и отправка писем. Это классический God Object.

Основные косяки:
- Метод create_order() на 28 строк - делает вообще все подряд
- Чтобы добавить новую скидку, надо лезть в код и добавлять if-ы (строки 27-28)
- SQL инъекция в строке 35 - просто вставляем данные в запрос через f-строку
- Тестировать это невозможно - все завязано друг на друга

По SOLID нарушается главное:
- **SRP нарушен** - один класс делает 5 разных вещей
- **OCP нарушен** - для новой скидки надо менять код
- **DIP нарушен** - напрямую создаем SMTP и работаем с БД

Посчитал цикломатическую сложность create_order - вышло 10 (куча if-ов и циклов). Норма - до 5, так что это плохо.

## Что сделал

Разбил один большой класс на несколько маленьких:

1. **UserValidator** - проверяет пользователей
2. **InventoryService** - работает с товарами
3. **PriceCalculator** - считает цену с налогами
4. **OrderRepository** - сохраняет заказы в БД
5. **NotificationService** - отправляет уведомления
6. **DiscountStrategy** - паттерн для скидок

Для скидок сделал Strategy pattern - теперь каждая скидка это отдельный класс (PercentageDiscount, FixedDiscount, NoDiscount). Чтобы добавить новую скидку, просто создаю новый класс - не надо менять существующий код.

Теперь OrderManager просто координирует работу этих классов - он стал намного проще (цикломатическая сложность 2 вместо 10).

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
