# Задание 2: Template Method - генераторы отчетов

## Анализ проблем

### Клоны кода (Code Clones)

#### Type II - Структурные клоны
Два класса `SalesReportGenerator` и `InventoryReportGenerator` имеют почти идентичную структуру с разными именами переменных и типами данных.

**Дублированные элементы:**

1. **Структура конструктора** (идентична в обоих классах):
```java
private DatabaseConnection db;
private Logger logger;
private EmailService emailService;

public Constructor(DatabaseConnection db, Logger logger, EmailService emailService) {
    this.db = db;
    this.logger = logger;
    this.emailService = emailService;
}
```

2. **Общий алгоритм метода generate():**
   - Создание StringBuilder
   - Добавление заголовка (строки 16-17 в SalesReportGenerator, строки 16-17 в InventoryReportGenerator)
   - Добавление периода (строка 18 в обоих)
   - Запрос данных из БД (строки 20-21 в обоих)
   - Проверка на пустоту (строки 23-26 в обоих)
   - Обработка данных в цикле
   - Логирование (строка 34 в SalesReportGenerator, строка 34 в InventoryReportGenerator)
   - Отправка email (строка 35 в обоих)
   - Возврат результата (строка 37 в обоих)

3. **Идентичная обработка пустых данных:**
```java
if (data.isEmpty()) {
    sb.append("No data\n");
    return sb.toString();
}
```

**Процент дублирования:** ~70% кода идентичен или очень похож.

### Проблемы проектирования

#### 1. Нарушение DRY (Don't Repeat Yourself)
Общий алгоритм генерации отчета дублируется в каждом классе.

#### 2. Shotgun Surgery
Для изменения процесса генерации отчета (например, добавление нового этапа обработки) нужно модифицировать каждый класс генератора.

#### 3. Жесткая привязка к формату
Формат вывода (текст с StringBuilder) захардкоден в методе. Нельзя легко изменить формат на CSV или HTML.

#### 4. Отсутствие гибкости в постобработке
Логирование и отправка email жестко встроены в метод generate(). Нельзя добавить архивирование или другие этапы без изменения кода.

### Метрики

#### WMC (Weighted Methods per Class) - ДО

**SalesReportGenerator:**
- Метод `generate()`: сложность 3 (1 if, 1 for, 1 базовая)
- WMC = 3

**InventoryReportGenerator:**
- Метод `generate()`: сложность 2 (1 if, 1 for)
- WMC = 2

**Общая WMC для системы: 5**

## Решение

(Будет добавлено после рефакторинга)

## UML-диаграммы

(Будут добавлены после рефакторинга)

## Как запустить

```bash
cd task2-template-method/after
javac *.java
java Main
```

Примечание: Код написан валидно, но для запуска требуется установленная JDK.
