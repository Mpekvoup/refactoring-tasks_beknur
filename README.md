# Рефакторинг кода: Практические задания

Репозиторий содержит 5 заданий по рефакторингу кода с применением принципов SOLID и паттернов проектирования.

## Структура проекта

```
refactoring-tasks/
├── task1-god-object/          # God Object - OrderManager (Python)
├── task2-template-method/     # Template Method - генераторы отчетов (Java)
├── task3-state-pattern/       # State Pattern - торговый автомат (Python)
├── task4-extract-class/       # Extract Class - Employee (Java)
└── task5-builder-decorator/   # Builder + Decorator - HttpRequest (Python)
```

Каждое задание содержит:
- `before/` - исходный код до рефакторинга
- `after/` - рефакторированный код
- `tests/` - unit и интеграционные тесты
- `diagrams/` - UML-диаграммы (Mermaid)
- `README.md` - анализ, решение, метрики

## Задания

### Задание 1: God Object - OrderManager
**Язык:** Python
**Проблема:** Класс с избыточной ответственностью (управление заказами, пользователями, инвентарем, email, БД)
**Решение:** Разделение на 5+ классов, применение паттерна Strategy для скидок
**Метрики:** Цикломатическая сложность до/после

### Задание 2: Template Method - генераторы отчетов
**Язык:** Java
**Проблема:** Дублирование кода в генераторах отчетов
**Решение:** Template Method + Strategy для форматов + Chain of Responsibility
**Метрики:** WMC (Weighted Methods per Class)

### Задание 3: State Pattern - торговый автомат
**Язык:** Python
**Проблема:** Множественные if/elif для проверки состояний
**Решение:** Паттерн State с отдельными классами состояний
**Метрики:** Диаграмма состояний, интеграционные тесты переходов

### Задание 4: Extract Class - Employee
**Язык:** Java
**Проблема:** Data Clumps - группы связанных полей в одном классе
**Решение:** Выделение Value Objects (BankDetails, Address), Move Method
**Метрики:** LCOM (Lack of Cohesion of Methods)

### Задание 5: Builder + Decorator - HttpRequest
**Язык:** Python
**Проблема:** Телескопический конструктор с 12+ параметрами, битовые флаги
**Решение:** Builder для создания объектов + Decorator для middleware
**Метрики:** Бенчмарк производительности

## Принципы работы

1. **Git-коммиты** - каждый логический этап фиксируется отдельным коммитом
2. **Формат коммитов** - `task{N}: краткое описание` (на русском)
3. **Минимум 4-5 коммитов** на каждое задание
4. **Тесты** - обязательны для всех заданий (pytest для Python, JUnit для Java)
5. **UML-диаграммы** - в формате Mermaid (до и после рефакторинга)
6. **Метрики** - конкретные числа в таблице "до/после"

## Как запустить

### Python (задания 1, 3, 5)
```bash
cd task{N}-название
pytest tests/
```

### Java (задания 2, 4)
```bash
cd task{N}-название
# Компиляция и запуск тестов (инструкции в README задания)
```

## Цель проекта

Изучение практических техник рефакторинга:
- Принципы SOLID
- Code Smells (God Object, Long Method, Data Clumps и др.)
- Паттерны проектирования (Strategy, Template Method, State, Builder, Decorator)
- Метрики качества кода
- TDD и автоматическое тестирование

---

**Автор:** Beknur
**Репозиторий:** https://github.com/Mpekvoup/refactoring-tasks_beknur
