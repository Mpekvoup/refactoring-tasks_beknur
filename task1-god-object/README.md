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

(Будет добавлено после рефакторинга)

## UML-диаграммы

(Будут добавлены после рефакторинга)

## Как запустить тесты

```bash
cd task1-god-object
pytest tests/
```
