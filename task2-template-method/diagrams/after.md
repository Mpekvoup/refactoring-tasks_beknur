# UML-диаграмма классов ПОСЛЕ рефакторинга

```mermaid
classDiagram
    class AbstractReportGenerator {
        <<abstract>>
        #db: DatabaseConnection
        #formatter: ReportFormatter
        #postProcessHandler: ReportHandler
        +generate(from, to): String
        #getTitle(): String*
        #fetchData(from, to): List~T~*
        #formatRow(item): String*
        #addSummary(data): String*
        #getRecipient(): String*
    }

    class SalesReportGenerator {
        +getTitle(): String
        +fetchData(from, to): List~Sale~
        +formatRow(item): String
        +addSummary(data): String
        +getRecipient(): String
    }

    class InventoryReportGenerator {
        +getTitle(): String
        +fetchData(from, to): List~Item~
        +formatRow(item): String
        +addSummary(data): String
        +getRecipient(): String
    }

    class FinancialReportGenerator {
        +getTitle(): String
        +fetchData(from, to): List~Transaction~
        +formatRow(item): String
        +addSummary(data): String
        +getRecipient(): String
    }

    class ReportFormatter {
        <<interface>>
        +format(title, from, to, content, summary): String
        +formatEmpty(title, from, to): String
    }

    class TextFormatter {
        +format(...): String
        +formatEmpty(...): String
    }

    class CsvFormatter {
        +format(...): String
        +formatEmpty(...): String
    }

    class HtmlFormatter {
        +format(...): String
        +formatEmpty(...): String
    }

    class ReportHandler {
        <<abstract>>
        #nextHandler: ReportHandler
        +setNext(handler): ReportHandler
        +handle(report, recipient): void
        #process(report, recipient): void*
    }

    class LogHandler {
        -logger: Logger
        +process(report, recipient): void
    }

    class EmailHandler {
        -emailService: EmailService
        +process(report, recipient): void
    }

    class ArchiveHandler {
        -archivePath: String
        +process(report, recipient): void
    }

    AbstractReportGenerator <|-- SalesReportGenerator
    AbstractReportGenerator <|-- InventoryReportGenerator
    AbstractReportGenerator <|-- FinancialReportGenerator
    AbstractReportGenerator --> ReportFormatter
    AbstractReportGenerator --> ReportHandler

    ReportFormatter <|.. TextFormatter
    ReportFormatter <|.. CsvFormatter
    ReportFormatter <|.. HtmlFormatter

    ReportHandler <|-- LogHandler
    ReportHandler <|-- EmailHandler
    ReportHandler <|-- ArchiveHandler
    ReportHandler --> ReportHandler: nextHandler
```
