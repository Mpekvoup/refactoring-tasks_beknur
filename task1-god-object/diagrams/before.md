# UML-диаграмма классов ДО рефакторинга

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
