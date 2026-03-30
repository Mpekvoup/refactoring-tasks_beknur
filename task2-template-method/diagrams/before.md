# UML-диаграмма классов ДО рефакторинга

```mermaid
classDiagram
    class SalesReportGenerator {
        -db: DatabaseConnection
        -logger: Logger
        -emailService: EmailService
        +generate(from, to): String
    }

    class InventoryReportGenerator {
        -db: DatabaseConnection
        -logger: Logger
        -emailService: EmailService
        +generate(from, to): String
    }

    SalesReportGenerator --> DatabaseConnection
    SalesReportGenerator --> Logger
    SalesReportGenerator --> EmailService
    InventoryReportGenerator --> DatabaseConnection
    InventoryReportGenerator --> Logger
    InventoryReportGenerator --> EmailService
```
